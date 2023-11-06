use coffee::{
    graphics::{Frame, Window},
    Timer,
};
use serde::{self, Deserialize, Serialize};

use crate::GameInfo;

pub trait Script {
    fn init(&self) {}
    fn update(&self) {}
}

#[typetag::serde(tag = "type")]
pub trait Bean {
    /// If your bean depends on other child beans to operate, then feed them in through here. Otherwise, it's fine to return an empty vec
    fn return_dependencies(&mut self) -> &mut Vec<Box<dyn Bean>>;

    /// Calls all of the initiation methods on a bean to reduce boilerplate. Override to change the functionality and remove unneeded calls on your per case basis to improve performance.
    fn _init_calls(&mut self, game_info: &GameInfo, window: &Window) {
        self.init(game_info);

        for dep in self.return_dependencies() {
            dep.init(game_info);

            dep._init_calls(game_info, window);

            dep.ready(game_info);
        }

        self.ready(game_info);
    }

    /// Calls all of the update methods on a bean to reduce boilerplate. Override to change the functionality and remove unneeded calls on your per case basis to improve performance.
    fn _update_calls(&mut self, window: &Window, game_info: &GameInfo) {
        self.early_update(game_info);

        for dep in self.return_dependencies() {
            dep._update_calls(window, &game_info);
        }

        self.update(&game_info);
    }

    /// Calls all of the draw methods on a bean to reduce boilerplate. Override to change functionality and remove unneeded calls on your per case basis to improve performance.
    fn _draw_calls(&mut self, game_info: &GameInfo, frame: &mut Frame, timer: &Timer) {
        for bean in self.return_dependencies() {
            bean._draw_calls(game_info, frame, timer);
        }

        self.draw(game_info, frame, timer)
    }

    /// Runs once when the bean enters the scope, will be called before all of it's scripts are finished
    #[allow(unused_variables)]
    fn init(&mut self, game_info: &GameInfo) {}
    
    /// Runs once after the bean enters the scope, but unlike init(), it will only be called after all the children have run their init and ready functions
    #[allow(unused_variables)]
    fn ready(&self, game_info: &GameInfo) {}
    
    /// Will be called once per frame, but is called before all children have run update() and earlyUpdate()
    #[allow(unused_variables)]
    fn early_update(&self, game_info: &GameInfo) {}

    /// Will be called once per frame, is called after all children have run update()
    #[allow(unused_variables)]
    fn update(&mut self, game_info: &GameInfo) {}

    #[allow(unused_variables)]
    fn draw(&self, game_info: &GameInfo, frame: &mut Frame, timer: &Timer) {}

    #[allow(unused_variables)]
    fn debug(&self, game_info: &GameInfo, frame: &mut Frame, timer: &Timer) {}
}

#[derive(Serialize, Deserialize)]
struct MinBean {
    pub dependencies: Vec<Box<dyn Bean>>,
}

#[typetag::serde]
impl Bean for MinBean {
    fn return_dependencies(&mut self) -> &mut Vec<Box<dyn Bean>> {
        &mut self.dependencies
    }
}
