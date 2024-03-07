//! The [`Scene`] component, which allows managment of loading and unloading entities and components dynamically.
//! It can also serialize and deserialize component data and instantiate entities using it to provide full building functionality.

use crate::scene::serialized_scene::SerializedSceneData;
use crate::scene::traits::SceneData;

use super::error;
use super::serialized_scene;
use super::serialized_scene::DataHashmap;
use super::serialized_scene::EntityHashmap;
use super::traits;

use bevy_ecs::component::Component;
use bevy_ecs::entity::Entity;
use bevy_ecs::world::World;

use bevy_reflect::serde::ReflectSerializer;
use bevy_reflect::TypeRegistry;
use inquire::Text;
use serde::Serialize;
use serde_json::Value;

use std::collections::HashMap;
use std::fs::File;
use std::io::Write;
use std::path::PathBuf;

/// Entity managment for loading and unloading in batches rather than having everything loaded at once.
///
/// Each [`Entity`] must have the [`SceneData`] component if it wishes to be managed by a scene.
///
/// If you'd rather have your entities not managed by a scene, you can simply omit the [`SceneData`] component.
///
/// `entities_initialized`: if the scene has been deserialized but the entities have not been spawned, this will be false.
/// Otherwise, this should always be true.
///
/// The comparison operator (`==`) is supported, but because comparing entities requires a [`World`] to obtain component data, using it only compares the names.
/// If you want a true eq operation that checks if the entities match, use [`Scene`]`::entity_eq()`. This does require [`World`] access though.
#[derive(Debug, Component, Clone)]
pub struct Scene {
    /// The name of the scene
    ///
    /// Primarily used for serialization, but can also be handy for organization and managing active scenes.
    ///
    /// Ideally, no two scenes should share the same name. Handling that is the responsibility of the [`SceneManager`]
    pub name: String,
    /// Contains an [`Entity`] id for every entity that this [`Scene`] is responsible for.
    /// Be careful when manually adjusting which entities are stored,
    /// since every entity is required to own one [`SceneData`] component.
    ///
    /// Using the API to add or remove entities ensures that every entity has a [`SceneData`] component,
    /// and ensures that no entity is orphaned and never unloaded. (unless requested)
    pub(crate) entities: Vec<Entity>,
    /// The path where the scene's save data is stored when calling [`save_scene`]
    pub(crate) save_data_path: Option<PathBuf>,
}

impl Scene {
    /// Creates a new blank [`Scene`] using the provided name.
    ///
    /// Does not contain any [`Entity`]'s and does not load any. To do that, wait until its ready.
    /// // TODO: When done, update these docs
    pub fn new(name: String) -> Self {
        Self {
            name,
            entities: Vec::new(),
            save_data_path: None,
        }
    }

    /// The comparison operator (`==`) but with entity comparison.
    /// This checks every entity to see if their [`SceneData`] matches, and if not, returns `false`.
    ///
    /// If you don't want to compare [`Scene`]s with world access, you can use the default `==` operator implementation.
    /// However, it will only compare the scene's IDs, so entity checking is not viable.'/:`12`
    pub fn entity_eq(&self, other: &Scene, world: &World) -> bool {
        if self.name != other.name {
            return false;
        }

        for i in 0..self.entities.len() {
            let self_entity = if let Some(entity) = other.entities.get(i) {
                world
                    .entity(entity.to_owned())
                    .get::<traits::SceneData>()
                    .unwrap()
                    .scene_id
            } else {
                return false;
            };

            let other_entity = if let Some(entity) = self.entities.get(i) {
                world
                    .entity(entity.to_owned())
                    .get::<traits::SceneData>()
                    .unwrap()
                    .scene_id
            } else {
                return false;
            };

            if self_entity != other_entity {
                return false;
            }
        } // entities presumed to match after this point

        true
    }

    pub fn get_entity(&self, world: &World, name: String) -> Option<Entity> {
        for entity in &self.entities {
            if world.get::<SceneData>(*entity).unwrap().object_name == name {
                return Some(*entity);
            }
        }
        None
    }

    pub fn get_entities(&self) -> &Vec<Entity> {
        &self.entities
    }

    pub fn save_data_path(&self) -> Option<&PathBuf> {
        self.save_data_path.as_ref()
    }
}

impl PartialEq for Scene {
    /// Compares the names of the two scenes to check if they are the same scene.
    ///
    /// Incredibly fallible, but works reasonably within the confines of the [`Scene`] system
    fn eq(&self, other: &Self) -> bool {
        self.name == other.name
    }
}

/// Serializes all of the entities with their components and stores it to a file (currently a temporary one)
pub fn save_scene(
    entity: Entity,
    world: &mut World,
    registry: &TypeRegistry,
) -> Result<(), error::SceneError> {
    let f = || PathBuf::from(Text::new("Save data path? >").prompt().unwrap());
    let path = &world
        .get::<Scene>(entity)
        .unwrap()
        .save_data_path
        .as_ref()
        .cloned()
        .unwrap_or_else(f);

    let new_file = match File::create(path) {
        Ok(ok) => ok,
        Err(err) => return Err(error::SceneError::IOError(err.to_string())),
    };

    let value = to_serialized_scene(world, registry, entity);

    if let Err(err) = serde_json::to_writer(new_file, &value.unwrap()) {
        return Err(error::SceneError::IOError(err.to_string()));
    }

    Ok(())
}

/// Creates a new scene component and spawns an entity with it
///
/// Does no validation to check if it shares a name, that's on the caller of the function
pub fn new_scene(world: &mut World, name: String) -> Entity {
    let scene = Scene::new(name);
    let entity = world.spawn(scene).id();
    entity
}

pub fn load_scene(
    path: PathBuf,
    world: &mut World,
    registry: &TypeRegistry,
) -> Result<Entity, error::SceneError> {
    use std::io::prelude::*;
    let mut buf = String::new();
    let _s = File::open(path)
        .map_err(|err| -> error::SceneError { error::SceneError::IOError(err.to_string()) })?
        .read_to_string(&mut buf)
        .unwrap();
    let deserialize = serde_json::from_str::<SerializedSceneData>(&buf)
        .map_err(|err| error::SceneError::LoadFailure(err.to_string()))?;
    let scene_entity = deserialize.initialize(world, registry)?;

    world.get_mut::<Scene>(scene_entity).unwrap().save_data_path = Some(buf.into());

    Ok(scene_entity)
}

/// Instantly despawns every entity belonging to the scene before despawning the scene entity.
///
/// Does not give any time or calls any methods on or before despawn.
/// If you want that, use a better (currently non-existent) method.
/// // fix that later maybe
///
/// Does not save before unloading! Make sure to call [`save_scene`] if anything in the scene must be serialized and stored.
/// If you don't have any non-global game state contained inside though, you're free to ignore that and unload as you please.
pub fn unload_scene(scene_entity: Entity, world: &mut World) {
    for entity in world.get::<Scene>(scene_entity).unwrap().entities.clone() {
        world.despawn(entity.to_owned());
    }
    world.despawn(scene_entity);
}

/// Adds a new entity to the scene
///
/// This function takes several steps to validate the entity before appending to the list.
/// * Ensures that the component has a [`SceneData`] component. If it doesn't, then one gets added automatically.
/// * Checks that no other entity in the scene has the same [`SceneData`] name. If there is, it will be adjusted to ensure absolute uniqueness of names.
pub fn add_entity_to_scene<'a>(
    world: &'a mut World,
    scene_entity: Entity,
    entity_to_add: Entity,
) -> Result<(), String> {
    // Very specific way this following code is blocked, since we need a list of entity names that DOESN'T include the entity currently being added
    let mut entity_names: Vec<String> = Vec::new();
    for (component, entity) in world.query::<(&mut SceneData, Entity)>().iter(world) {
        if !world
            .get::<Scene>(scene_entity)
            .unwrap()
            .entities
            .contains(&entity)
        {
            continue;
        }
        entity_names.push(component.object_name.to_owned());
    }

    if let None = world.get::<SceneData>(entity_to_add) {
        let object_name = String::from("New entity");

        world.entity_mut(entity_to_add).insert(traits::SceneData {
            object_name,
            scene_id: 0, // TODO: Make use of scene_ids or get rid of them idk why i added them
        });
    }

    validate_name(
        &mut entity_names.iter(),
        &mut world
            .get_mut::<SceneData>(entity_to_add)
            .unwrap()
            .object_name,
    );

    let mut scene_entity = World::entity_mut(world, scene_entity);
    let mut scene = scene_entity.get_mut::<Scene>().unwrap();

    scene.entities.push(entity_to_add.clone());

    Ok(())
}

/// Runs through the list of names, and checks to see if the name is a duplicate of any inside the list
///
/// If it is, the function will automatically append a new ID and try again.
///
/// Operation is currently worst case of `O(n^2)`
pub fn validate_name(names: &mut dyn Iterator<Item = &String>, name_to_check: &mut String) {
    let mut i = 0;
    loop {
        let mut contains = false;
        for name in &mut *names {
            if name == name_to_check {
                contains = true;
                break;
            }
        }

        if contains == false {
            break;
        }

        println!("{:?} contains {}", "Som", &name_to_check);

        let suffix = format!("({})", i);
        *name_to_check = name_to_check.strip_suffix(&suffix).unwrap_or("").to_owned();
        i += 1;
        name_to_check.push_str(&format!("({})", i))
    }
}

// TODO: Fix documentation
/// Creates a [`SerializableScene`] using the scene's component data
pub fn to_serialized_scene<'a>(
    world: &'a mut World,
    registry: &TypeRegistry,
    scene_entity: Entity,
) -> Result<serialized_scene::SerializedSceneData, String> {
    let scene_entity_list: Vec<Entity> = world
        .entity(scene_entity)
        .get::<Scene>()
        .unwrap()
        .entities
        .clone();

    let mut entity_data: DataHashmap = HashMap::new();

    for (entity, serializable_components_data) in world
        .query::<(Entity, &dyn traits::TestSuperTrait)>()
        .iter(world)
    {
        if !scene_entity_list.contains(&entity) {
            continue;
        }

        let mut entity_hashmap: EntityHashmap = HashMap::new();

        for component in serializable_components_data.iter() {
            let component_serialized_data: Vec<u8> = Vec::new();

            // To swap out serializers, simply replace serde_json::Serializer with another serializer of your choice
            let formatter = serde_json::ser::PrettyFormatter::with_indent("    ".as_bytes());
            let mut serializer =
                serde_json::Serializer::with_formatter(component_serialized_data, formatter);

            if let Err(err) =
                ReflectSerializer::new(component.as_reflect(), registry).serialize(&mut serializer)
            {
                panic!(
                    "Failed to serialize `{}` component! [{}]",
                    component.as_reflect().reflect_type_path(),
                    err.to_string()
                )
            }

            let serialized_component_json = serializer.into_inner();

            let check_string = check_string(serialized_component_json).unwrap();

            let from_str: HashMap<String, HashMap<String, Value>> =
                serde_json::from_str(&check_string).unwrap();

            to_writer(&check_string);

            let component_name_hashmap = from_str.iter().next().unwrap();

            entity_hashmap.insert(
                component_name_hashmap.0.to_owned(),
                component_name_hashmap.1.to_owned(),
            );
        }
        let k = world.get::<SceneData>(entity).unwrap().object_name.clone();

        entity_data.insert(k, entity_hashmap);
    }

    let scene = world.get_mut::<Scene>(scene_entity).unwrap();
    Ok(serialized_scene::SerializedSceneData {
        name: scene.name.clone(),
        entity_data,
    })
}

fn check_string(
    serialized_data_from_entity: Vec<u8>,
) -> Result<String, Result<SerializedSceneData, String>> {
    Ok(match String::from_utf8(serialized_data_from_entity) {
        Ok(string) => string,
        Err(err) => return Err(Err(err.to_string())),
    })
}

fn to_writer(to_string: &str) {
    let mut path_buf = std::env::current_dir().unwrap();
    path_buf.pop();
    path_buf.push("test_output");
    path_buf.push("scene_serialization.json");
    let _ = File::create(path_buf).unwrap().write(to_string.as_bytes());
}
