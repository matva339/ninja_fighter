pub mod render_type;

use bevy_ecs::system::Query;
use bevy_ecs::system::ResMut;
use ggez::graphics::{self as ggraphics, *};

use engine::space;
use engine::GgezInterface;

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

        renderer.set(
            renderer.draw_param.transform(draw_transform),
            Position::new(0.0, 0.0),
        )
    }
}

pub fn draw(query: Query<&Renderer>, mut main_canvas: ResMut<GgezInterface>) {
    for renderer in query.iter() {
        let canvas_option = main_canvas.get_canvas_mut();

        let mut canvas = match canvas_option {
            Some(canvas) => canvas,
            None => return,
        };

        match &renderer.image {
            RenderType::Image(image) => {
                ggraphics::Canvas::draw(&mut canvas, image, renderer.draw_param)
            }
            RenderType::InstanceArray(_) => todo!(),
            RenderType::Mesh(_) => todo!(),
            RenderType::Text(_) => todo!(),
        }
    }
}

#[derive(bevy_ecs::component::Component)]
pub struct Renderer {
    pub draw_param: DrawParam,
    pub image: RenderType,
    pub offset: space::Position,
    pub transform: Transform,
}

#[allow(dead_code)]
impl Renderer {
    /// Creates a new basic Renderer component for regular use.
    /// Use `Renderer::set()` to alter the offset and extra draw settings, or `Renderer::new_opt()` to directly set those values during initialization.
    pub fn new(image: RenderType, transform: Transform) -> Self {
        let draw_param = DrawParam {
            src: Default::default(),
            color: Color::WHITE,
            transform: transform.into(),
            z: 0,
        };
        let offset = space::Position::new(0.0, 0.0);

        Renderer {
            image,
            draw_param,
            transform,
            offset,
        }
    }

    /// Similar to `Renderer::new()`, but with extra parameters for other values.
    pub fn new_opt(
        image: RenderType,
        transform: Transform,
        draw_param: DrawParam,
        offset: space::Position,
    ) -> Self {
        Renderer {
            image,
            draw_param,
            transform,
            offset,
        }
    }

    pub fn set(&mut self, draw_param: DrawParam, offset: space::Position) {
        self.draw_param = draw_param;
        self.offset = offset;
    }
}

#[allow(dead_code)]
impl Renderer {
    pub fn default(gfx: &GraphicsContext) -> Self {
        Self {
            image: RenderType::default(gfx),
            draw_param: Default::default(),
            transform: Default::default(),
            offset: Default::default(),
        }
    }
}
