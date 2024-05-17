pub mod render_type;

use std::ops::Deref;

use bevy_ecs::component::Component;
use bevy_ecs::prelude::*;
use bevy_ecs::system::Query;
use bevy_ecs::system::Res;
use bevy_ecs::system::ResMut;
use bevy_reflect::Reflect;
use bevy_reflect::Struct;
use engine::editor::FieldWidget;
use engine::scene::CustomSerialization;
use engine::Camera;
use ggez::graphics::{self as ggraphics, *};

use engine::space;
use engine::GgezInterface;
use ggraphics::Canvas;
use log::trace;
use serde::Deserialize;
use serde::Serialize;

use self::render_type::RenderType;

use engine::space::Transform;

use engine::space::*;

type TransformComponentTuple<'a> = (
    &'a Position,
    &'a Velocity,
    &'a Rotation,
    &'a Scale,
    &'a TransformSettings,
);

pub fn update(mut query: Query<(&mut Renderer, TransformComponentTuple)>) {
    for (mut renderer, transform) in &mut query {
        let draw_transform: ggez::graphics::Transform = Transform {
            position: dbg!(transform.0.to_owned()),
            velocity: transform.1.to_owned(),
            rotation: transform.2.to_owned(),
            scale: transform.3.to_owned(),
            settings: transform.4.to_owned(),
        }
        .into();

        renderer.draw_param.transform = draw_transform.clone();

        let draw_param = renderer.draw_param.to_owned();

        Renderer::set(&mut renderer, draw_param, Vector2::new(0.0, 0.0))
    }
}

pub fn draw(
    query: Query<(&Renderer, TransformComponentTuple)>,
    mut main_canvas: ResMut<GgezInterface>,
    camera: Res<Camera>,
) {
    for (renderer, transform) in query.iter() {
        let canvas_option = main_canvas.get_canvas_mut();

        let canvas = match canvas_option {
            Some(canvas) => canvas,
            None => return,
        };

        if let Some(renderimage) = &renderer.image {
            match renderimage {
                RenderType::Image(image) => {
                    draw_image(canvas, image, renderer, transform, &camera);
                }
                RenderType::InstanceArray(_) => todo!(),
                RenderType::Mesh(_) => todo!(),
                RenderType::Text(_) => todo!(),
                RenderType::None => (),
                RenderType::Quad(quad) => canvas.draw(
                    quad,
                    renderer.draw_param.dest::<mint::Point2<f32>>(mint::Point2 {
                        x: transform.0.x,
                        y: transform.0.y,
                    }),
                ),
            }
        }
    }
}

fn draw_image(
    canvas: &mut Canvas,
    image: &Image,
    renderer: &Renderer,
    transform: TransformComponentTuple,
    camera: &Camera,
) {
    let mut transformer = DEFAULT_TRANSFORM.clone();

    transformer.position = {
        (*transform
            .0
            .to_owned()
            .translate(&renderer.offset)
            .translate(&-*camera.position))
        .into()
    };

    let mut draw_param = renderer.draw_param.clone();

    draw_param.transform = transformer.into();

    canvas.draw(image, draw_param)
}

#[derive(Component, Reflect, Default, Clone, Serialize, Deserialize)]
#[reflect(Component)]
pub struct Renderer {
    #[serde(serialize_with = "engine::render::serialize_draw_param")]
    #[serde(deserialize_with = "engine::render::deserialize_draw_param")]
    #[reflect(ignore)]
    pub draw_param: ggez::graphics::DrawParam,
    #[serde(skip)]
    #[reflect(ignore)]
    pub image: Option<RenderType>,
    pub offset: space::Vector2,
}

impl FieldWidget for Renderer {
    fn ui(value: &mut dyn Reflect, ui: &mut egui::Ui) {
        let field_value = value.downcast_mut::<Self>().unwrap(); //you can use this if your type implements reflect

        match &mut field_value.image {
            Some(some) => {
                some.ui(ui);
            }
            None => {
                if ui.button("Set to prototype renderer").clicked() {
                    field_value.image = Some(RenderType::Quad(ggraphics::Quad));
                    field_value.draw_param = DrawParam {
                        src: Rect {
                            x: 0.0,
                            y: 0.0,
                            w: 20.0,
                            h: 20.0,
                        },
                        color: Color::BLUE,
                        transform: Transform::default().into(),
                        z: 0,
                    }
                }
            }
        };

        ui.collapsing("Draw Param", |ui| {
            let draw_param = &mut field_value.draw_param;

            ui.collapsing("src", |ui| {
                ui.add(egui::DragValue::new(&mut draw_param.src.x));
                ui.add(egui::DragValue::new(&mut draw_param.src.y));
                ui.add(egui::DragValue::new(&mut draw_param.src.w));
                ui.add(egui::DragValue::new(&mut draw_param.src.h));
            });

            let rgba = draw_param.color.to_rgba();
            let color_label = ui.label("Color");
            let mut color32 = egui::Color32::from_rgba_unmultiplied(rgba.0, rgba.1, rgba.2, rgba.3);
            ui.color_edit_button_srgba(&mut color32)
                .labelled_by(color_label.id);
            draw_param.color(ggraphics::Color::from_rgba(
                color32.r(),
                color32.g(),
                color32.b(),
                color32.a(),
            ));

            ui.collapsing("Transform", |ui| match &mut draw_param.transform {
                ggraphics::Transform::Values {
                    dest,
                    rotation,
                    scale,
                    offset,
                } => {
                    ui.add(egui::DragValue::new(&mut dest.x));
                    ui.add(egui::DragValue::new(&mut dest.y));
                    ui.add(egui::DragValue::new(&mut scale.x));
                    ui.add(egui::DragValue::new(&mut scale.y));
                }
                ggraphics::Transform::Matrix(matrix) => {
                    ui.label("transform is matrix, which is currently unsupported");
                }
            });

            let z_label = ui.label("z");
            ui.add(egui::DragValue::new(&mut draw_param.z))
                .labelled_by(z_label.id);
        });
    }
}

#[allow(dead_code)]
impl Renderer {
    /// Creates a new basic Renderer component for regular use.
    /// Use `Renderer::set()` to alter the offset and extra draw settings, or `Renderer::new_opt()` to directly set those values during initialization.
    pub fn new(image: Option<RenderType>, transform: Transform) -> Self {
        let draw_param = DrawParam {
            src: Default::default(),
            color: Color::WHITE,
            transform: transform.into(),
            z: 0,
        };

        let offset = space::Vector2::new(0.0, 0.0);

        Renderer {
            image,
            draw_param,
            offset,
        }
    }

    /// Similar to `Renderer::new()`, but with extra parameters for other values.
    pub fn new_opt(
        image: Option<RenderType>,
        draw_param: DrawParam,
        offset: space::Vector2,
    ) -> Self {
        Renderer {
            image,
            draw_param,
            offset,
        }
    }

    pub fn set(&mut self, draw_param: DrawParam, offset: space::Vector2) {
        self.draw_param = draw_param;
        self.offset = offset;
    }
}

impl CustomSerialization for Renderer {
    fn serialize_data(
        type_data: &engine::scene::CustomSerializationData,
        value: &dyn Reflect,
    ) -> serde_json::Map<String, serde_json::Value> {
        let value = value.downcast_ref::<Self>().unwrap();

        let mut map = serde_json::Map::new();

        let draw_param = value.field("draw_param").unwrap();
        let mut draw_param_map = serde_json::Map::new();
        draw_param_map.insert("src".to_owned(), "test".into());
        map.insert(
            "draw_param".to_owned(),
            serde_json::Value::Object(draw_param_map),
        );

        map
    }
}
