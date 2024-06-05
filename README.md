# Ninja Fighter Engine
## I think I'm just sticking with this as the engine name :D

A game engine that prioritizes flexibility and ease of development.

To use it, it requires a bit of effort in getting it set up.

To make a game with it, first create a new package and add the following code to the binary file:
```
static ENGINE_CONFIG: engine::EngineConfig = engine::EngineConfig::default();

fn main() {
    let (mut context, event_loop) = // you can use the engine re-export of ggez, though I reccomend adding it anyways
        engine::ggez::ContextBuilder::new("name_of_game", "Author Name")
            .build()
            .expect("could not build context?!");

    let mut game_root = engine::GameRoot::new(&mut context, &ENGINE_CONFIG)
        .expect("expected no errors on game root initialization");

    editor::console::hook_emergency_panic_handler(&mut game_root);

    engine::ggez::event::run(context, event_loop, game_root);
}
```

From there, dive into the engine documentation to feel your way around all of the features of the engine.
