use super::EditorTabTypes;

use log::*;

use super::Response;

use super::InspectorWindow;

#[derive(Debug, Default)]
pub struct EntityViewState {}

pub fn draw_entities(
    ui: &mut egui::Ui,
    tab: &mut <InspectorWindow as egui_dock::TabViewer>::Tab,
) -> Option<Response> {
    if tab_state.entities.len() == 0 {
        ui.label("No entities found!");
    }
    for (name, entity) in &tab_state.entities {
        if ui.small_button(name).clicked() {
            trace!("Clicked entity");
            tab_state.focused_entity = Some((entity.clone(), name.clone()));
            return Some(Response::SwitchToTab(EditorTabTypes::Inspector));
        }
    }
    None
}