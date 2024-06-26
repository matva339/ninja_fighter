use bevy_ecs::schedule::*;
use components::*;
use engine::{schedule::ScheduleTag, EngineConfig};
use log::*;

pub static INITIAL_SCENE: &str = "game/assets/scenes/Theo Matthew Game.json";
pub static SCENE_FOLDER: &str = "game/assets/scenes/";

pub static ENGINE_CONFIG: EngineConfig = EngineConfig {
    external_scene_paths: &[INITIAL_SCENE],
    scenes_folder: Some(SCENE_FOLDER),
    world_init: init_components_and_resources,
    ticks_per_second: 60,
    freeze_on_unfocus: false,
    freeze_on_minimize: true,
    run_debug_schedules: false,
};

pub fn init_components_and_resources(world: &mut bevy_ecs::world::World) {
    components::initialize_component_types(world);
    trace!("Registered component types");

    world.add_schedule(tick_schedule());
    world.add_schedule(frame_schedule());
    world.add_schedule(freeze_tick_schedule());
    world.add_schedule(init_schedule());
    trace!("Created and inserted ECS schedules");
}

pub fn tick_schedule() -> Schedule {
    let mut sched = Schedule::new(ScheduleTag::Tick);
    // Configuration block
    sched
        .set_build_settings(TICK_SETTINGS.clone())
        .set_executor_kind(ExecutorKind::MultiThreaded)
        .add_systems(
            (
                // components::collider::mesh_editor::update_editor,
                protag::protag_update,
                engine::space::update,
                collider::collider_update,
            )
                .chain(),
        );

    sched
}

pub fn freeze_tick_schedule() -> Schedule {
    let mut sched = Schedule::new(ScheduleTag::FreezeTick);
    // Configuration block
    sched
        .set_build_settings(TICK_SETTINGS.clone())
        .set_executor_kind(ExecutorKind::MultiThreaded)
        .add_systems((
            collider::collider_update,
            protag::protag_update,
            // components::collider::mesh_editor::update_editor,
        ));

    sched
}

pub fn frame_schedule() -> Schedule {
    let mut draw_sched = Schedule::new(ScheduleTag::Frame);
    draw_sched
        .set_build_settings(FRAME_SETTINGS.clone())
        .set_executor_kind(ExecutorKind::SingleThreaded);

    draw_sched.add_systems(
        (
            // insert draw systems here
            render::renderer_draw,
            components::collider::mesh_renderer::mesh_renderer_draw,
            components::text_renderer::render_text_renderers,
            // components::collider::mesh_editor::draw_editor_interface,
        )
            .chain(),
    );

    draw_sched
}

pub fn init_schedule() -> Schedule {
    let mut init_sched = Schedule::new(ScheduleTag::Init);

    init_sched
        .set_build_settings(INIT_SETTINGS.clone())
        .set_executor_kind(ExecutorKind::MultiThreaded);

    init_sched
        // .add_systems(debug::init)
        .add_systems(protag::protag_init);

    init_sched
}

pub(crate) static TICK_SETTINGS: ScheduleBuildSettings = ScheduleBuildSettings {
    ambiguity_detection: LogLevel::Warn,
    hierarchy_detection: LogLevel::Warn,
    use_shortnames: false,
    report_sets: true,
    auto_insert_apply_deferred: true,
};
pub(crate) static FRAME_SETTINGS: ScheduleBuildSettings = ScheduleBuildSettings {
    ambiguity_detection: LogLevel::Warn,
    hierarchy_detection: LogLevel::Warn,
    use_shortnames: false,
    report_sets: true,
    auto_insert_apply_deferred: true,
};
pub(crate) static INIT_SETTINGS: ScheduleBuildSettings = ScheduleBuildSettings {
    ambiguity_detection: LogLevel::Warn,
    hierarchy_detection: LogLevel::Warn,
    use_shortnames: false,
    report_sets: true,
    auto_insert_apply_deferred: true,
};
