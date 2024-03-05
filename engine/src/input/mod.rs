//! The input module for handling player input.
//!
//! To get started, read the docs for [`resource::Input`] to crawl your way around.
//!
//! # Structs
//! * [`Input`] - Input [`bevy_ecs::system::Resource`] that handles all interactions between [`ggez`] and user scripts through [`Action`]'s and [`Key`]'s.
//!
//! * [`Key`] - Minimal container for storing info about [`ggez::event`]'s.
//!
//! * [`Action`] - Basic container for assigning [`Key`]'s to user script actions.
//!
pub mod action;
pub mod key;
pub mod main;
pub mod resource;
#[cfg(test)]
mod test;

mod input_update_scheduler {
    pub(crate) struct InputUpdateScheduler {}

    impl InputUpdateScheduler {
        pub fn push_update(&mut self) {}
    }
}

pub use action::{Action, KeyStatus};
pub use ggez::input::keyboard::KeyCode;
pub use key::keycode_converter::KeycodeType;
pub use key::Key;
pub use main::main as input_cli_editor;
pub use resource::Input;
