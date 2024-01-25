use std::{
    env::current_dir,
    fmt::Display,
    fs::File,
    io::{BufWriter, Write},
    path::PathBuf,
};

use bevy_ecs::{
    bundle::Bundle,
    component::{Component, ComponentId},
    entity::Entity,
    system::{Command, Commands, EntityCommand, EntityCommands, Spawn},
    world::World,
};
use serde::{de::Visitor, ser::SerializeStruct, Deserialize, Serialize};

use std::{collections::HashMap, hash::Hash, sync::atomic::AtomicUsize};

use crate::scene;

#[derive(Debug, Bundle)]
pub struct SceneBundle {
    pub scene: Scene,
}

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
    pub name: String,
    pub entities: Vec<Entity>,
    /// When serializing a scene, the component data must be serialized before the `serialize()` component is run.
    /// Since `serialize()` can't take in a [`World`] during the functionality, it instead must be taken care of beforehand.
    /// This means the responsibility falls on the caller to take care of this before every serialization.
    /// To do so, a simple call to `Scene::`
    serialized_entity_component_data: Option<String>,
}

impl PartialEq for Scene {
    fn eq(&self, other: &Self) -> bool {
        self.name == other.name
    }
}

#[derive(Debug)]
pub struct SerializedScene {
    pub name: String,
    pub entity_data: String,
}

impl SerializedScene {
    pub fn initialize(self, world: &mut World) -> serde_json::Result<Scene> {
        let scene = Scene::new(self.name.to_owned());
        // TODO: Deserialize entity data here and add it to the scene

        let v: serde_json::Value = serde_json::from_str(&self.entity_data)?;
        let entity = world.spawn_empty();
        // for component in v.

        dbg!(v);

        Ok(scene)
    }
}

impl Scene {
    pub fn new(name: String) -> Self {
        Self {
            name,
            entities: Vec::new(),
        }
    }

    pub fn unload(&self, commands: &mut Commands) {
        for entity in &self.entities {
            commands.entity(entity.to_owned()).despawn();
        }
    }

    pub fn save(&self, world: &mut World) -> Result<(), std::io::Error> {
        let mut path = PathBuf::new();
        path.push(current_dir()?);
        let new_file = File::create(path)?;

        serde_json::to_writer(new_file, self)?;

        Ok(())
    }

    pub fn serialize_entity_components(&mut self, world: &mut World) -> Result<(), String> {
        for entity in self.entities {
            let scene_data = world.get::<SceneData>(entity).ok_or(format!(
                "Entity {:?} does not have a SceneData component!",
                entity
            ))?;

            scene_data.serializeable_components;
        }

        todo!()
    }

    /// The comparison operator (`==`) but with entity comparison.
    /// This checks every entity to see if their [`SceneData`] matches, and if not, returns `false`.
    ///
    /// If you don't want to compare [`Scene`]s with world access, you can use the default `==` operator implementation.
    /// However, it will only compare the scene's IDs, so entity checking is not viable.
    pub fn entity_eq(&self, other: &Scene, world: &mut World) -> bool {
        if self.name != other.name {
            return false;
        }

        for i in 0..self.entities.len() {
            let self_entity = if let Some(entity) = other.entities.get(i) {
                world
                    .entity(entity.to_owned())
                    .get::<SceneData>()
                    .unwrap()
                    .scene_id
            } else {
                return false;
            };

            let other_entity = if let Some(entity) = self.entities.get(i) {
                world
                    .entity(entity.to_owned())
                    .get::<SceneData>()
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
}

impl Serialize for Scene {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        let mut serialize_struct = serializer.serialize_struct("SerializedScene", 2)?;
        serialize_struct.serialize_field("name", &self.name);
        let var_name = serde_json::to_string(&self.entities).unwrap();
        serialize_struct.serialize_field("entity_data", &var_name);
        // TODO: Convert entites to string data that can be deserialized
        serialize_struct.end()
    }
}

impl<'de> Deserialize<'de> for SerializedScene {
    /// Takes in a [`SerializedScene`] struct made from [`Scene`]`::serialize()` and turns it back into a scene
    ///
    /// Required to call [`SerializedScene`]::initialize() to turn it back into a useable [`Scene`]
    fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
    where
        D: serde::Deserializer<'de>,
    {
        deserializer.deserialize_struct("SerializedScene", &["name", "entity_data"], SceneVisitor)
    }
}

struct SceneVisitor;
impl<'de> Visitor<'de> for SceneVisitor {
    type Value = SerializedScene;

    fn expecting(&self, formatter: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(formatter, "a serialized scene with an entities field")
    }

    fn visit_map<A>(self, mut map: A) -> Result<Self::Value, A::Error>
    where
        A: serde::de::MapAccess<'de>,
    {
        let mut scene = SerializedScene {
            name: String::new(),
            entity_data: String::new(),
        };

        // This at one point was like 20 lines long
        while let Some((key, value)) = map.next_entry::<String, String>()? {
            match key.as_str() {
                "name" => scene.name = value,
                "entity_data" => scene.entity_data = value,
                _ => (),
            };
        }
        todo!()
    }
}

#[derive(Debug, Eq, Clone, Copy)]
pub struct SceneObjectID {
    pub(crate) id: usize,
}

impl PartialEq for SceneObjectID {
    fn eq(&self, other: &Self) -> bool {
        self.id == other.id
    }
}

impl Hash for SceneObjectID {
    fn hash<H: std::hash::Hasher>(&self, state: &mut H) {
        self.id.hash(state);
    }
}

impl SceneObjectID {
    pub fn get_id() -> usize {
        pub(crate) static COUNTER: AtomicUsize = AtomicUsize::new(1);
        COUNTER.fetch_add(1, std::sync::atomic::Ordering::Relaxed)
    }
}

#[test]
fn scene_test() {
    let mut world = World::new();

    let init_scene: Scene = dbg!(Scene {
        name: String::from("TestScene"),
        entities: Vec::new(),
    });

    let to_string: String =
        dbg!(serde_json::to_string(&init_scene).expect("jesoon should have serialized properly"));

    let serialized_scene: SerializedScene =
        dbg!(serde_json::from_str::<SerializedScene>(&to_string)
            .expect("jesoon should have deserialized properly"));

    let result_scene: Scene =
        dbg!(SerializedScene::initialize(serialized_scene, &mut world).unwrap());

    assert!(Scene::entity_eq(&init_scene, &result_scene, &mut world))
}

pub struct SceneTag {
    scene_name: String,
}

#[derive(bevy_ecs::component::Component)]
pub struct SceneData {
    pub root_scene: String,
    pub serializeable_components: Vec<ComponentId>,
    pub scene_id: usize,
}

impl Serialize for Scene {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        let mut serialize_struct = serializer.serialize_struct("Scene", 2)?;
        serialize_struct.serialize_field("name", &self.name);
        let value: Vec<Entity> = Vec::new();
        serialize_struct.serialize_field("entities", &value);
        serialize_struct.end()
    }
}

impl<'de> Deserialize<'de> for Scene {
    fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
    where
        D: serde::Deserializer<'de>,
    {
        todo!()
    }
}
