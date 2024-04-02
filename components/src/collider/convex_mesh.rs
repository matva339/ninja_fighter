use bevy_ecs::prelude::*;
use bevy_reflect::Reflect;
use engine::space;
use engine::space::Position;
use engine::Camera;
use engine::GgezInterface;
use ggez::graphics;
use ggez::graphics::Color;
use ggez::graphics::DrawParam;
use ggez::graphics::GraphicsContext;
use ggez::graphics::MeshData;
use log::*;
use serde::ser::SerializeStruct;
use serde::Deserialize;
use serde::Serialize;

use std::ops::Deref;

use super::mesh_renderer::MeshRenderer;
use super::traits::CertifiableMesh;
use super::Collider;

/// Runs physics updates for collider meshes
pub fn update(
    mut query: Query<(&mut Collider, Option<&Position>)>,
    engine: Res<GgezInterface>,
    input: Res<engine::Input>,
) {
    for (mut collider, entity_position) in query.iter_mut() {
        let convex_mesh = collider.meshes.get_mut(0).unwrap();
        let entity_position = match entity_position {
            Some(pos) => pos,
            None => {
                log::error!("Position is required for collider_mesh component to update!");
                continue;
            }
        };
    }
}

/// Draws collider vertecies/edges if debug is enabled
pub fn draw(
    query: Query<(&Collider, &MeshRenderer)>,
    mut engine: ResMut<GgezInterface>,
    camera: Res<Camera>,
) {
    if !engine.is_debug_draw() {
        return;
    }

    for (collider, renderer) in query.iter() {
        let drawable = match collider.meshes.get(0).unwrap().into() {
            Some(mesh) => mesh.into_graphics_mesh(&engine.get_context().gfx),
            None => continue,
        };
        let canvas = engine
            .get_canvas_mut()
            .expect("ColliderMesh should only be called in a draw schedule");

        // initial param before applying camera offset, and maybe shaders later
        let initial_param = match &renderer.draw_param {
            Some(param) => param,
            None => continue,
        };

        // dont worry about it for now, just take those initial parameters
        let mut final_param = initial_param.clone();

        final_param.color(Color::CYAN);

        canvas.draw(&drawable, final_param);
    }
}

/// A mesh that works for collision.
///
/// The entire shape must be convex, i.e. each point must have a line of sight from the origin
///
/// [Demo](game\assets\demos\polygonmesh.png)
#[derive(Debug, Clone, Reflect, Default)]
pub struct ConvexMesh {
    pub(crate) position: space::Position,
    /// The vertices used to calculate where the mesh's corners are.
    ///
    /// Uses vector vertices, not graphic vertices.
    pub(crate) vertices: Vec<space::Vertex>,
}

impl ConvexMesh {
    pub fn new(vertices: Vec<space::Vertex>) -> Self {
        let mut convex_mesh = Self {
            vertices,
            position: Position::default(),
        };

        convex_mesh
            .build_indices()
            .map_err(|err| format!("Invalid indices build: {}", err))
            .unwrap();

        convex_mesh
    }

    pub fn add_vertex(&mut self, vertex: space::Vertex) {
        self.vertices.push(vertex);
    }

    pub fn add_debug_vertex(&mut self, vertex: graphics::Vertex) {
        self.vertices.push(space::Vertex::from(vertex));
    }

    pub fn pop_vertex(&mut self) {
        self.vertices.pop();
    }

    /// Checks to see if every vertex is convex.
    ///
    /// The idea is that it checks the angle between the origin and every vertex, and if the angle goes backwards, the triangle is invalid.
    /// Check out this [demo](game\assets\demos\polygonmesh.png) for more details.
    ///
    /// This makes it easier and more performant to render triangles.
    ///
    /// If the vertex is invalid, returns the index of the vertex that is invalid.
    ///
    /// If there are too few vertecies to make a triangle, returns zero.
    pub fn validate_convex(&self) -> Result<(), f32> {
        validate_vertices(&self.vertices)
    }

    /// Runs physics updates for collider meshes
    pub fn update(&mut self, position: &Position) {
        let translation_amount = *self.position.deref() - *position.deref();

        for vertex in &mut self.vertices {
            vertex.translate(&translation_amount);
        }
    }
}

impl CertifiableMesh for ConvexMesh {
    fn verify_vertices(&self) -> Result<(), String> {
        let vec = &self.vertices;
        let len = vec.len();
        if len < 3 {
            return Err(0.0.to_string());
        }
        let origin_vertex = vec[0];
        let mut previous_vertex = vec[1];
        let mut checking_vertex;

        let mut previous_angle = origin_vertex.inverse_sum(*previous_vertex).angle();

        for i in 2..len {
            checking_vertex = vec[i];

            let checking_angle = previous_vertex.inverse_sum(*checking_vertex).angle();
            let angle_difference = checking_angle - previous_angle;

            // if angle_difference > 0.0 {
            //     // TODO: make it less than or equal to when not doing box collider
            //     return Err(angle_difference);
            // }

            previous_angle = checking_angle;
            previous_vertex = checking_vertex;
        }
        Ok(())
    }

    /// Builds a vec of indices that correlate to how triangles are connected.
    ///
    /// For more info, check out [demo](game\assets\demos\polygonmesh.png).
    fn build_indices(&self) -> Result<Vec<u32>, String> {
        self.validate_convex().map_err(|v| v.to_string())?;

        build_convex_indices(self.vertices.len() as u32, Vec::new()).map_err(|v| v.to_string())
    }

    fn get_vertices_mut(&mut self) -> &mut Vec<space::Vertex> {
        &mut self.vertices
    }

    fn into_graphics_mesh(&self, gfx: &GraphicsContext) -> ggez::graphics::Mesh {
        graphics::Mesh::from_data(
            gfx,
            graphics::MeshData {
                vertices: &self
                    .vertices
                    .iter()
                    .map(|vtx| (*vtx).into())
                    .collect::<Vec<graphics::Vertex>>(),
                indices: &self.build_indices().unwrap(),
            },
        )
    }
}

/// Builds a vec of indices that correlate to how triangles are connected.
///
/// When calling this function, validate that the vertices are valid before attempting to build triangles with it.
/// This code assumes that you've already checked and that each triangle can be constructed from the index.
///
/// For more info, check out [demo](game\assets\demos\polygonmesh.png).
fn build_convex_indices(len: u32, mut vec: Vec<u32>) -> Result<Vec<u32>, u32> {
    for i in 0..len - 2 {
        vec.extend([0, 1 + i, 2 + i]);
    }

    Ok(vec)
}

/// Checks to see if every vertex is convex.
///
/// The idea is that it checks the angle between the origin and every vertex, and if the angle goes backwards, the triangle is invalid.
/// Check out this [demo](game\assets\demos\polygonmesh.png) for more details.
///
/// This makes it easier and more performant to render triangles.
///
/// If the vertex is invalid, returns the index of the vertex that is invalid.
///
/// If there are too few vertecies to make a triangle, returns zero.
pub fn validate_vertices(vec: &Vec<space::Vertex>) -> Result<(), f32> {
    let len = vec.len();
    if len < 3 {
        return Err(0.0);
    }
    let origin_vertex = vec[0];
    let mut previous_vertex = vec[1];
    let mut checking_vertex;

    let mut previous_angle = origin_vertex.inverse_sum(*previous_vertex).angle();

    for i in 2..len {
        // trace!("vtx#{}, prev angle: {}", i, previous_angle);
        checking_vertex = vec[i];

        let checking_angle = previous_vertex.inverse_sum(*checking_vertex).angle();
        let angle_difference = checking_angle - previous_angle;
        // assert_eq!(angle_difference, 90.0);

        // if angle_difference > 0.0 {
        //     // TODO: make it less than or equal to when not doing box collider
        //     return Err(angle_difference);
        // }

        previous_angle = checking_angle;
        previous_vertex = checking_vertex;
    }
    Ok(())
}

impl<'md> From<graphics::MeshData<'md>> for ConvexMesh {
    fn from(value: graphics::MeshData) -> Self {
        let vec = value
            .vertices
            .iter()
            .map(|value| space::Vertex::from(value))
            .collect::<Vec<space::Vertex>>();

        let position = Position::new(0.0, 0.0);

        Self {
            position,
            vertices: vec,
        }
    }
}

// Serialization

impl Serialize for ConvexMesh {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        let mut serialize_seq = serializer.serialize_struct("ColliderMesh", 3)?;
        serialize_seq.serialize_field("position", &self.position)?;
        serialize_seq.serialize_field("vertices", &self.vertices)?;
        serialize_seq.end()
    }
}

impl<'de> Deserialize<'de> for ConvexMesh {
    fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
    where
        D: serde::Deserializer<'de>,
    {
        deserializer.deserialize_struct(
            "ColliderMesh",
            &["position", "vertices"],
            ConvexMeshVisitor,
        )
    }
}

struct ConvexMeshVisitor;

impl<'de> serde::de::Visitor<'de> for ConvexMeshVisitor {
    type Value = ConvexMesh;

    fn expecting(&self, formatter: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(formatter, "Was expecting a collider mesh struct")
    }

    fn visit_str<E>(self, v: &str) -> Result<Self::Value, E>
    where
        E: serde::de::Error,
    {
        todo!()
    }
}

#[derive(Debug, Clone, Default)]
pub struct SerializedDrawMesh {
    pub vertices: Vec<graphics::Vertex>,
    pub indicies: Vec<u32>,
}

impl SerializedDrawMesh {
    fn into_mesh(self, gfx: &GraphicsContext) -> graphics::Mesh {
        graphics::Mesh::from_data(
            gfx,
            MeshData {
                vertices: &self
                    .vertices
                    .iter()
                    .map(|v| Into::<graphics::Vertex>::into(*v))
                    .collect::<Vec<graphics::Vertex>>(),
                indices: &self.indicies,
            },
        )
    }
}

impl Serialize for SerializedDrawMesh {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        let mut serialize_struct = serializer.serialize_struct("DrawMesh", 2)?;

        serialize_struct.serialize_field(
            "vertices",
            &self
                .vertices
                .iter()
                .map(|value| SerializableVertex::from(value))
                .collect::<Vec<SerializableVertex>>(),
        )?;
        serialize_struct.serialize_field("indices", &self.indicies)?;

        todo!();

        serialize_struct.end()
    }
}

#[derive(Debug, Serialize, Deserialize)]
struct SerializableVertex {
    position: [f32; 2],
    uv: [f32; 2],
    color: [f32; 4],
}

impl From<&graphics::Vertex> for SerializableVertex {
    fn from(value: &graphics::Vertex) -> Self {
        SerializableVertex {
            position: value.position,
            uv: value.uv,
            color: value.color,
        }
    }
}
