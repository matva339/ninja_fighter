use std::ops::Deref;

use crate::{collider::Collider, render::render_type::RenderType, render::Renderer};
use bevy_ecs::prelude::*;
use bevy_reflect::Reflect;
use engine::space::{Position, Transform, TransformSettings, Velocity};
use engine::GgezInterface;
use engine::{space, Input};
use ggez::graphics::{self, Color, DrawParam, Image, Rect};
use nalgebra::ComplexField;

pub fn init(mut commands: Commands, engine: Res<GgezInterface>) {
    commands.spawn(ProtagBundle::new(&engine));
}

#[derive(Default, Component, Reflect)]
pub struct Protag;

#[derive(Bundle)]
pub struct ProtagBundle {
    protag: Protag,
    controller: ProtagController,
    transform: Transform,
    renderer: Renderer,
    collider: Collider,
}

#[derive(Default, Debug, Component, Reflect)]
#[reflect(Component)]
pub struct ProtagController {
    pub acc: f32,
    pub decel: f32,
    pub jump_power: f32,
    pub speed_cap: f32,
    pub fall_acc: f32,
    pub max_fall_speed: f32,
}

pub fn update(
    mut query: Query<(&mut Position, &mut Velocity, &ProtagController)>,
    input: Res<Input>,
    ggez: Res<GgezInterface>,
) {
    let height = ggez.get_context().gfx.size().1;

    for (mut pos, mut velocity, controller) in query.iter_mut() {
        if velocity.x.abs() > controller.speed_cap {
            velocity.x -= (controller.decel) * (velocity.x / velocity.x.abs());
        }

        if is_moving(WASD::D, &input) && velocity.x < controller.speed_cap {
            velocity.x += controller.acc;
        } else if is_moving(WASD::A, &input) && velocity.x > -controller.speed_cap {
            velocity.x -= controller.acc;
        } else {
            velocity.x *= 1.0 - controller.decel
        }
        if is_moving(WASD::W, &input) {
            velocity.y -= 0.3;
        }
        if is_moving(WASD::S, &input) {
            velocity.y += 0.3;
        }
        if (pos.y > 370.0 || true) && input.get_action("Click").unwrap().is_just_pressed() {
            velocity.y = -controller.jump_power;
            velocity.x *= 1.2;
            velocity.x = velocity
                .x
                .clamp(-controller.speed_cap * 1.2, controller.speed_cap * 1.2);
        }
        if velocity.y < controller.max_fall_speed && pos.y < height - 110.0 {
            velocity.y += controller.fall_acc;
        } else if pos.y > height - 100.0 && velocity.y >= 0.0 {
            velocity.y = 0.0;
            pos.y = height - 100.0
        }
    }
}

enum WASD {
    W,
    A,
    S,
    D,
}

fn is_moving(direction: WASD, input: &Input) -> bool {
    input
        .get_action(match direction {
            WASD::W => "Up",
            WASD::A => "Left",
            WASD::S => "Down",
            WASD::D => "Right",
        })
        .unwrap()
        .status()
        .is_held()
}

impl ProtagBundle {
    pub fn new(engine: &GgezInterface) -> Self {
        let protag = Protag {};

        let transform = Transform {
            position: space::Position::new(10.0, 10.0),
            velocity: space::Velocity::default(),
            rotation: space::Rotation::default(),
            scale: space::Scale::default(),
            settings: TransformSettings { auto_update: true },
        };

        let gfx = &GgezInterface::get_context(&engine).gfx;
        let mut renderer = Renderer::new(
            RenderType::Image(Image::from_color(gfx, 100, 100, Some(Color::RED))),
            transform.into(),
        );
        renderer.set(
            DrawParam {
                src: Rect::new_i32(10, 10, 1, 1),
                color: graphics::Color::WHITE,
                transform: transform.into(),
                z: 0,
            },
            space::Position::new(10.0, 0.0),
        );

        let collider = Collider::new(engine);

        let controller = ProtagController {
            acc: 0.5,
            decel: 0.08,
            jump_power: 10.0,
            speed_cap: 8.0,
            fall_acc: 0.5,
            max_fall_speed: 10.0,
        };
        Self {
            protag,
            transform,
            renderer,
            collider,
            controller,
        }
    }
}
