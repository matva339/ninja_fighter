use std::any::Any;
use std::collections::HashMap;

use bevy_ecs::identifier::error;
use bevy_ecs::reflect::ReflectComponent;
use bevy_ecs::reflect::ReflectFromWorld;
use bevy_ecs::world::Mut;
use bevy_ecs::world::World;
use bevy_reflect::DynamicStruct;
use bevy_reflect::DynamicTupleStruct;
use bevy_reflect::Enum;
use bevy_reflect::Reflect;
use bevy_reflect::ReflectKind;
use bevy_reflect::Struct;
use bevy_reflect::TupleStruct;
use bevy_reflect::TypeInfo;
use bevy_reflect::TypeRegistration;
use bevy_reflect::TypeRegistry;
use bevy_utils::Duration;
use convert_case::Casing as _;
use egui::ComboBox;
use egui::Label;
use egui::LayerId;
use egui::Layout;
use egui::Pos2;
use egui::Rect;
use egui::Sense;
use engine::editor::InspectableAsField;
use engine::scene::ReflectTestSuperTrait;
use engine::scene::SceneManager;
use log::*;

use super::InspectorWindow;
use super::Response;

#[derive(Debug, Default)]
pub struct InspectorViewState {
    adding_component: bool,
}

pub(super) fn draw_inspector(
    state: &mut InspectorWindow,
    ui: &mut egui::Ui,
    tab: &mut <InspectorWindow as egui_dock::TabViewer>::Tab,
) -> Option<Response> {
    if state.focused_entity.is_none() {
        ui.label("No entity in focus");
        return None;
    }

    let entity = state.focused_entity.clone().unwrap();

    let debug_mode = state.debug_mode;

    ui.label("Inspecting ".to_owned() + &entity.1);

    let Some(component_ids) = state.components.get(&entity.0).cloned() else {
        ui.label("(Components Unavailable)".to_owned());

        error!("Could not find component data for {}", &entity.1);
        return None;
    };

    state
        .world()
        .resource_scope(|world, res: Mut<SceneManager>| {
            for c_id in component_ids.iter() {
                let Some(component_info) = world.components().get_info(*c_id) else {
                    error!("Could not find component {:?} on {}", c_id, entity.1);
                    return;
                };

                let component_type_id = component_info.clone().type_id().unwrap();

                let type_registration = res
                    .type_registry
                    .get(component_type_id)
                    .expect("expected a type registration for component");

                let Some(mut get_entity_mut) = world.get_entity_mut(entity.0) else {
                    error!("Could not find entity in world");
                    return;
                };

                let Some(mut ptr) = get_entity_mut.get_mut_by_id(*c_id) else {
                    error!("Could not get untyped component from ComponentID.");
                    return;
                };

                let reflected = unsafe {
                    let val = ptr.as_mut();

                    type_registration
                        .data::<bevy_reflect::ReflectFromPtr>()
                        .unwrap()
                        .as_reflect_mut(val)
                };

                assert_eq!(reflected.as_reflect().type_id(), component_type_id);
                // SAFETY: ptr is of type type_id as required in safety contract, type_id was checked above
                // also, I'm totally taking "inspiration" from `bevy-inspector-egui`. Go check it out, it's awesome :D

                let type_path = reflected.reflect_type_path().to_owned();

                let display_path = match debug_mode {
                    true => type_path,
                    false => type_path
                        .split("::")
                        .collect::<Vec<&str>>()
                        .pop()
                        .unwrap()
                        .to_string()
                        .to_case(convert_case::Case::Title),
                };

                if let bevy_reflect::ReflectMut::Struct(s) = reflected.reflect_mut() {
                    if s.field_len() == 0 {
                        if let Some(inspectable) = type_registration.data::<InspectableAsField>() {
                            inspectable.show(ui, s.as_reflect_mut());
                            if !debug_mode {
                                continue;
                            }
                        };
                        ui.label(display_path.clone());
                    } else {
                        ui.collapsing(display_path.clone(), |ui| {
                            if let Some(inspectable) =
                                type_registration.data::<InspectableAsField>()
                            {
                                inspectable.show(ui, s.as_reflect_mut());
                                if !debug_mode {
                                    return;
                                }
                            };
                            draw_struct_in_inspector(s, ui, &res.type_registry, debug_mode);
                        });
                    }
                };
                if let bevy_reflect::ReflectMut::TupleStruct(ts) = reflected.reflect_mut() {
                    ui.collapsing(display_path.clone(), |ui| {
                        if let Some(inspectable) = type_registration.data::<InspectableAsField>() {
                            inspectable.show(ui, ts.as_reflect_mut());
                            if !debug_mode {
                                return;
                            }
                        };
                        draw_tuple_struct_in_inspector(ts, ui, &res.type_registry, debug_mode);
                    });
                };
                if let bevy_reflect::ReflectMut::Enum(e) = reflected.reflect_mut() {
                    if let Some(inspectable) = type_registration.data::<InspectableAsField>() {
                        inspectable.show(ui, e.as_reflect_mut());
                        if !debug_mode {
                            continue;
                        }
                    };
                    draw_enum_in_inspector(e, ui, &res.type_registry, debug_mode);
                };
            }
        });

    ui.add(egui::Separator::default());

    ui.collapsing("Add components", |ui| {
        let modules = &state.component_modules.clone();
        let world = state.world(); // pulled out into variable so that formatter wouldnt add an extra tab of indentation for no reason like why is it so much
        world.resource_scope(|world: &mut World, res: Mut<SceneManager>| {
            for module in modules {
                ui.collapsing(module.0.clone(), |ui| {
                    for (component, type_) in module.1 {
                        if let Some(c_id) = world.components().get_id(type_.type_id()) {
                            if component_ids.contains(&c_id) {
                                continue;
                            }
                        }

                        let display_path = match debug_mode {
                            true => {
                                component.1.clone()
                            },
                            false => {
                                component.1.split("::").collect::<Vec<&str>>().pop().unwrap().to_string()
                            },
                        };

                        if ui.button(display_path).clicked() {
                            trace!("Clicked on component add button");

                            let reflect_component = match type_.data::<ReflectComponent>() {
                                Some(some) => some,
                                None => {
                                    log::error!(
                                        "Couldnt find ReflectComponent type data for {}.
                                        (Perhaps you're missing the #[reflect(Component) macro attribute)",
                                        component.1
                                    );

                                    continue;
                                }
                            };

                            let mut entity_mut = world.entity_mut(entity.0);

                            trace!("Setting values for fields in component");

                            match type_.type_info() {
                                TypeInfo::Struct(s) => {
                                    let mut bundle = DynamicStruct::default();

                                    trace!("Setting represented type to iterate over expected fields for type info");

                                    bundle.set_represented_type(Some(type_.type_info()));

                                    log::trace!("Iterating over fields to ensure field types have type info stored");
                                    for field in s.iter() {
                                        let value =
                                            res.type_registry.get_type_info(field.type_id());

                                        if value.is_none() {
                                            log::error!(
                                                "{} has no obtainable type info in the registry!",
                                                field.name()
                                            );
                                            return;
                                        }
                                    }

                                    // for field in bundle.iter_fields() {
                                    //     println!("{:#?}", field);
                                    // }
                                    // log::info!("itered fields");

                                    reflect_component.apply_or_insert(
                                        &mut entity_mut,
                                        &bundle,
                                        &res.type_registry,
                                    );
                                }
                                TypeInfo::TupleStruct(ts) => {
                                    let mut bundle = DynamicTupleStruct::default();

                                    bundle.set_represented_type(Some(type_.type_info()));

                                    reflect_component.apply_or_insert(
                                        &mut entity_mut,
                                        &bundle,
                                        &res.type_registry,
                                    );
                                }
                                TypeInfo::Enum(e) => todo!(),
                                _ => unreachable!(),
                            }

                            log::info!(
                                "Added {} to {}",
                                type_.type_info().type_path_table().short_path(),
                                entity.1
                            );
                        }
                    }
                });
            }
        });
    });

    None
}

fn draw_struct_in_inspector(
    structure: &mut dyn Struct,
    ui: &mut egui::Ui,
    type_registry: &TypeRegistry,
    debug_mode: bool,
) {
    let Some(some) = structure.get_represented_type_info().cloned() else {
        error!(
            "Could not get type info for {}",
            structure.reflect_type_path()
        );
        return;
    };
    let TypeInfo::Struct(struct_info) = some else {
        error!(
            "Invalid type info for {}, this is not a struct",
            structure.reflect_type_path()
        );
        return;
    };

    let striped = egui::Grid::new(structure.reflect_type_path())
        .num_columns(2)
        .striped(true);

    striped.show(ui, |ui: &mut egui::Ui| {
        for field_name in struct_info.field_names() {
            let name = field_name.to_owned();

            let field_mut = Struct::field_mut(structure, name);

            let Some(field) = field_mut else {
                // this error log is breaking rustfmt >:(
                // log::error!("Invalid field data: Field {} exists in type data, but not in the reflected struct.", field_name);
                continue;
            };

            let display_name = match debug_mode {
                true => field_name.to_string(),
                false => field_name.to_case(convert_case::Case::Title),
            };
            if let Some(type_data) =
                type_registry.get_type_data::<InspectableAsField>(field.as_reflect().type_id())
            {
                ui.label(display_name);
                ui.scope(|ui: &mut egui::Ui| {
                    type_data.show(ui, field);
                });
                ui.end_row();
                continue;
            }

            ui.scope(|ui: &mut egui::Ui| {
                match field.reflect_mut() {
                    bevy_reflect::ReflectMut::Struct(s) => {
                        draw_struct_in_inspector(s, ui, type_registry, debug_mode);
                    }
                    bevy_reflect::ReflectMut::TupleStruct(ts) => {
                        draw_tuple_struct_in_inspector(ts, ui, type_registry, debug_mode);
                    }
                    bevy_reflect::ReflectMut::Tuple(t) => todo!(),
                    bevy_reflect::ReflectMut::List(l) => todo!(),
                    bevy_reflect::ReflectMut::Array(a) => todo!(),
                    bevy_reflect::ReflectMut::Map(m) => todo!(),
                    bevy_reflect::ReflectMut::Enum(e) => {
                        draw_enum_in_inspector(e, ui, type_registry, debug_mode);
                    }
                    bevy_reflect::ReflectMut::Value(v) => {
                        ui.label(display_name);

                        ui.label(format!(
                            "(No inspector implementation for {})",
                            v.reflect_type_path()
                        ));
                    }
                };
            });

            ui.end_row();
        }
    });
}

fn draw_tuple_struct_in_inspector(
    structure: &mut dyn TupleStruct,
    ui: &mut egui::Ui,
    type_registry: &TypeRegistry,
    debug_mode: bool,
) {
    let Some(some) = structure.get_represented_type_info().cloned() else {
        error!(
            "Could not get type info for {}",
            structure.reflect_type_path()
        );
        return;
    };
    let TypeInfo::TupleStruct(struct_info) = some else {
        error!(
            "Invalid type info for {}, this is not a struct",
            structure.reflect_type_path()
        );
        return;
    };

    for unnamed_field in struct_info.iter() {
        let name = unnamed_field.to_owned();

        let field_mut = TupleStruct::field_mut(structure, unnamed_field.index());

        let Some(field) = field_mut else {
            error!("Invalid field data: Field at {} exists in type data, but not in the reflected struct.", unnamed_field.index());
            continue;
        };

        let Some(type_data) =
            type_registry.get_type_data::<InspectableAsField>(field.as_reflect().type_id())
        else {
            error!(
                "Could not find inspector data for type [{}] for field at index [{}]",
                field.reflect_type_path(),
                unnamed_field.index()
            );
            continue;
        };

        ui.scope(|ui: &mut egui::Ui| {
            match field.reflect_mut() {
                bevy_reflect::ReflectMut::Struct(s) => {
                    draw_struct_in_inspector(s, ui, type_registry, debug_mode)
                }
                bevy_reflect::ReflectMut::TupleStruct(ts) => {
                    draw_tuple_struct_in_inspector(ts, ui, type_registry, debug_mode)
                }
                bevy_reflect::ReflectMut::Tuple(t) => todo!(),
                bevy_reflect::ReflectMut::List(l) => todo!(),
                bevy_reflect::ReflectMut::Array(a) => todo!(),
                bevy_reflect::ReflectMut::Map(m) => todo!(),
                bevy_reflect::ReflectMut::Enum(e) => todo!(),
                bevy_reflect::ReflectMut::Value(v) => {
                    type_data.show(ui, v);
                }
            };
        });
    }
}

fn draw_enum_in_inspector(
    structure: &mut dyn Enum,
    ui: &mut egui::Ui,
    type_registry: &TypeRegistry,
    debug_mode: bool,
) -> Option<egui::Response> {
    ComboBox::new("Enum", "Not supported").show_ui(ui, |ui| todo!());

    todo!()
}
