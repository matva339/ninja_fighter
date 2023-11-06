pub mod assets;
pub mod bean;
pub mod bean_types;
pub mod cup;

use std::collections::HashMap;

use assets::Assets;
use coffee::input::keyboard::KeyCode;
use coffee::input::KeyboardAndMouse;
use coffee::load::loading_screen::ProgressBar;
use cup::{BeanGrinder, Cup};

use coffee::graphics::{Color, Frame, Window, WindowSettings};
use coffee::load::Task;
use coffee::{Game, Result, Timer};

fn main() -> Result<()> {
    GameRoot::run(WindowSettings {
        title: String::from("Ninja Fighter [PROTOTYPE]"),
        size: (100 * 16, 100 * 9),
        resizable: true,
        fullscreen: false,
        maximized: false,
    })
}

#[allow(dead_code)]
pub struct GameRoot {
    pub cup: Cup,
    pub game_info: GameInfo,
}

pub struct GameInfo {
    pub assets: Assets,
    pub delta: f32,
}

impl Game for GameRoot {
    type Input = KeyboardAndMouse;
    type LoadingScreen = ProgressBar; // No loading screen

    const TICKS_PER_SECOND: u16 = 60;
    const DEBUG_KEY: Option<KeyCode> = Some(KeyCode::F12);

    fn load(_window: &Window) -> Task<GameRoot> {
        let assets: Assets = Assets {
            internal_assets: HashMap::new(),
        };

        let cup: Cup = BeanGrinder::brew_default_cup();
        let delta: f32 = 1.0 / GameRoot::TICKS_PER_SECOND as f32;
        let game_info: GameInfo = GameInfo { assets, delta };

        Task::succeed(move || GameRoot { cup, game_info })
    }

    fn draw(&mut self, frame: &mut Frame, timer: &Timer) {
        frame.clear(Color::WHITE);

        for bean in self.cup.pour_beans() {
            bean._draw_calls(&self.game_info, frame, timer);
        }
    }

    fn interact(&mut self, _input: &mut Self::Input, _window: &mut Window) {}

    fn update(&mut self, _window: &Window) {
        for bean in &mut self.cup.beans {
            bean._update_calls(_window, &self.game_info);
        }
    }

    fn cursor_icon(&self) -> coffee::graphics::CursorIcon {
        coffee::graphics::CursorIcon::Default
    }

    fn debug(&self, _input: &Self::Input, frame: &mut Frame<'_>, debug: &mut coffee::Debug) {
        debug.draw(frame);
    }

    fn on_close_request(&mut self) -> bool {
        true
    }

    fn is_finished(&self) -> bool {
        false
    }
}
