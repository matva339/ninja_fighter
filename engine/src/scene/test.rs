#![allow(unused_imports)]
use crate::{
    scene::{
        component::{self, Scene},
        object_data::{SceneData, TestSuperTrait},
        scene_manager::SceneManager,
        serialized_scene::SerializedSceneData,
    },
    space::transform,
};
use bevy_ecs::{
    component::{Component, ComponentDescriptor},
    reflect::ReflectComponent,
    world::World,
};
use bevy_reflect::{TypeRegistration, TypeRegistry};
use bevy_trait_query::TraitQuery;
use serde::Serialize;
use std::{any::TypeId, fs::File, io::Write};

#[derive(Debug, Clone, Component, Serialize, Default, bevy_reflect::Reflect)]
#[reflect(Component)]
struct TestComponent {
    serialize_value_1: String,
    serialize_value_2: i32,
}

#[derive(Debug, Clone, Component, Serialize, Default, bevy_reflect::Reflect)]
#[reflect(Component)]
struct TestComponent2 {
    ineedafunnynameforthis: String,
    peepeedoodookaka: bool,
    the_real_test: char,
    float: f64,
}

impl TraitQuery for TestComponent {}

#[test]
fn scene_test() {
    // Init world
    let mut world = World::new();

    world.init_component::<TestComponent>();
    world.init_component::<TestComponent2>();

    // Init component traits for querying
    use bevy_trait_query::RegisterExt;
    world.register_component_as::<dyn TestSuperTrait, TestComponent>();
    world.register_component_as::<dyn TestSuperTrait, TestComponent2>();

    let mut registry = TypeRegistry::default();
    registry.register::<SceneData>();
    registry.register::<TestComponent>();
    registry.register::<TestComponent2>();
    registry
        .get_type_info(TypeId::of::<TestComponent>())
        .unwrap()
        .type_path();

    crate::register_scene_types(&mut world);

    // Init scene
    let scene_component: Scene = Scene::new("TestScene".to_string());
    let scene_entity_id = World::spawn(&mut world, scene_component).id();

    // At an unknown amount of time later, create an entity
    let test_entity = world.spawn(transform::Transform::default()).id().clone();

    let test_component = TestComponent {
        serialize_value_1: String::from("My name is :3"),
        serialize_value_2: 654101, // sixty ie fo te ti
    };

    world.entity_mut(test_entity).insert(test_component);

    // Another one for good measure
    let test_entity2 = world.spawn(transform::Transform::default()).id().clone();

    world.entity_mut(test_entity2).insert(TestComponent {
        serialize_value_1: String::from("My name is :3c"),
        serialize_value_2: 4226363,
    });

    world.entity_mut(test_entity).insert(TestComponent2 {
        ineedafunnynameforthis: String::new(),
        peepeedoodookaka: true,
        the_real_test: ' ',
        float: 29.000,
    });

    // Add the test entitys to the scene
    let scene_entity = World::entity_mut(&mut world, scene_entity_id).id();

    if let Err(err) = component::add_entity_to_scene(&mut world, scene_entity, test_entity, None) {
        panic!("Adding entity failed! [{}]", err)
    }
    if let Err(err) = component::add_entity_to_scene(&mut world, scene_entity, test_entity2, None) {
        panic!("Adding entity failed! [{}]", err)
    }

    // Serialize the scene
    let entity_mut = World::entity_mut(&mut world, scene_entity).id();

    let serialized_scene =
        match component::create_serializable_scene_data(&mut world, &registry, entity_mut) {
            Ok(serialized_scene) => serialized_scene,
            Err(err) => panic!("Serializing scene failed! [{}]", err),
        };

    let msg = "jesoon should have serialized properly";
    let to_string: String = serde_json::to_string(&serialized_scene).expect(msg);

    println!(
        "The stringified jesoon, to be stored in file: {}",
        to_string
    );

    // Save txt for analysis
    let mut path_buf = std::env::current_dir().unwrap();
    path_buf.pop();
    path_buf.push("test_output");
    path_buf.push("scene_serialization.json");
    println!("{}", path_buf.to_str().unwrap());
    let _ = File::create(path_buf).unwrap().write(to_string.as_bytes());

    // Pretend we make some sys calls to retrieve that data here
    let msg = "jesoon should have deserialized properly";
    let serialized_scene: SerializedSceneData =
        serde_json::from_str(&to_string.clone()).expect(msg);

    // Initialize scene using the retrieved data
    let result_entity =
        SerializedSceneData::initialize(serialized_scene, &mut world, &registry).unwrap();

    let result_scene: &Scene = world.get(result_entity).unwrap();

    // Double check that the scene serialized and deserialized properly
    let initial_scene: &Scene = world.get(scene_entity_id).unwrap();
    let var = Scene::entity_eq(initial_scene, &result_scene, &world);
    if var {
        dbg!(initial_scene);
        dbg!(result_scene);
        dbg!(world);
    }
    assert!(var); // Fails if serde_json::from_str::<SerializedScene>(&to_string.clone()) returns incorrect scene data.
}
