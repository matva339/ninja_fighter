use std::fs::File;
use std::io::prelude::*;
use std::path::PathBuf;

use crate::input::Action;

use super::Input;

/// Welcome to the input CLI editor! Here you can create new keys and alter the input data from the command line!
/// Mostly useful early on when setting things up.
pub fn main() -> ! {
    println!("Booting into input editor..");
    println!("\nWelcome to the input editor!");

    let mut key_file: File;
    let mut action_file: File;
    let mut input_module: Input = Input::new();
    loop {
        println!(">");
        let mut io_input = String::new();
        if let Err(err) = std::io::stdin().read_line(&mut io_input) {
            println!("Could not figure out what you asked, try again. Use `help` to see possible commands. ({})", err);
            continue;
        }

        io_input = io_input.to_lowercase();

        io_input.pop();
        io_input.pop();

        if io_input == String::from("help") {
            help()
        } else if io_input == String::from("save") {
            save()
        } else if io_input == String::from("load") {
            load(&mut input_module)
        } else if io_input == String::from("add_key") {
            add_key()
        } else if io_input == String::from("edit_key") {
            edit_key()
        } else if io_input == String::from("remove_key") {
            remove_key()
        } else if io_input == String::from("add_action") {
            add_action()
        } else if io_input == String::from("edit_action") {
            edit_action()
        } else if io_input == String::from("remove_action") {
            remove_action()
        } else if io_input == String::from("exit") {
            std::process::exit(0)
        } else {
            println!("Invalid input.")
        }
    }
}

fn help() {
    println!(
        "
Welcome to my humble abode

No help is currently available, you'll have to pour through the code yourself

Sorry :\
    "
    )
}

fn save() {
    todo!()
}

fn load(input: &mut Input) {
    let dir = match std::env::current_dir() {
        Ok(path) => path,
        Err(err) => panic!("Path directory error! What? {}", err),
    };

    let key_path = dir.join(PathBuf::from("/src/input/keyData.txt"));
    let mut key_file = match std::fs::File::open(key_path) {
        Ok(path) => path,
        Err(err) => panic!("Key file could not be opened! {}", err),
    };

    let mut buf = String::new();
    match key_file.read_to_string(&mut buf) {
        Ok(_) => (),
        Err(err) => panic!("Invalid file read! {}", err),
    }

    *input = Input::from(buf);
}

fn add_key() {
    todo!()
}

fn edit_key() {
    todo!()
}

fn remove_key() {
    todo!()
}

fn add_action() {
    todo!()
}

fn edit_action() {
    todo!()
}

fn remove_action() {
    todo!()
}
