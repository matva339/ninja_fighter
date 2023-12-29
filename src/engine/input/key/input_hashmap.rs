use super::super::action::KeyStatus;
use super::super::key::keycode_converter;
use super::super::key::keycode_converter::KeycodeType;
use super::super::key::Key;
use super::KeyCode;
use crate::engine::input::key::stringcode::StringifiableKeyCode;
use std::collections::HashMap;
use std::sync::OnceLock;

pub(crate) enum InputFile {
    KeyFile,
    ActionFile,
}

pub(crate) fn const_key_hashmap() -> &'static HashMap<KeycodeType, Key> {
    static HASHMAP: OnceLock<HashMap<KeycodeType, Key>> = OnceLock::new();
    HASHMAP.get_or_init(|| {
        let mut hash_map = HashMap::new();
        {
            let keyvalue_pairs: Vec<KeycodeType> = vec![
                (KeycodeType::Keyboard(KeyCode::Key1)),
                (KeycodeType::Keyboard(KeyCode::Key2)),
                (KeycodeType::Keyboard(KeyCode::Key3)),
                (KeycodeType::Keyboard(KeyCode::Key4)),
                (KeycodeType::Keyboard(KeyCode::Key5)),
                (KeycodeType::Keyboard(KeyCode::Key6)),
                (KeycodeType::Keyboard(KeyCode::Key7)),
                (KeycodeType::Keyboard(KeyCode::Key8)),
                (KeycodeType::Keyboard(KeyCode::Key9)),
                (KeycodeType::Keyboard(KeyCode::Key0)),
                (KeycodeType::Keyboard(KeyCode::A)),
                (KeycodeType::Keyboard(KeyCode::B)),
                (KeycodeType::Keyboard(KeyCode::C)),
                (KeycodeType::Keyboard(KeyCode::D)),
                (KeycodeType::Keyboard(KeyCode::E)),
                (KeycodeType::Keyboard(KeyCode::F)),
                (KeycodeType::Keyboard(KeyCode::G)),
                (KeycodeType::Keyboard(KeyCode::H)),
                (KeycodeType::Keyboard(KeyCode::I)),
                (KeycodeType::Keyboard(KeyCode::J)),
                (KeycodeType::Keyboard(KeyCode::K)),
                (KeycodeType::Keyboard(KeyCode::L)),
                (KeycodeType::Keyboard(KeyCode::M)),
                (KeycodeType::Keyboard(KeyCode::N)),
                (KeycodeType::Keyboard(KeyCode::O)),
                (KeycodeType::Keyboard(KeyCode::P)),
                (KeycodeType::Keyboard(KeyCode::Q)),
                (KeycodeType::Keyboard(KeyCode::R)),
                (KeycodeType::Keyboard(KeyCode::S)),
                (KeycodeType::Keyboard(KeyCode::T)),
                (KeycodeType::Keyboard(KeyCode::U)),
                (KeycodeType::Keyboard(KeyCode::V)),
                (KeycodeType::Keyboard(KeyCode::W)),
                (KeycodeType::Keyboard(KeyCode::X)),
                (KeycodeType::Keyboard(KeyCode::Y)),
                (KeycodeType::Keyboard(KeyCode::Z)),
                (KeycodeType::Keyboard(KeyCode::Escape)),
                (KeycodeType::Keyboard(KeyCode::F1)),
                (KeycodeType::Keyboard(KeyCode::F2)),
                (KeycodeType::Keyboard(KeyCode::F3)),
                (KeycodeType::Keyboard(KeyCode::F4)),
                (KeycodeType::Keyboard(KeyCode::F5)),
                (KeycodeType::Keyboard(KeyCode::F6)),
                (KeycodeType::Keyboard(KeyCode::F7)),
                (KeycodeType::Keyboard(KeyCode::F8)),
                (KeycodeType::Keyboard(KeyCode::F9)),
                (KeycodeType::Keyboard(KeyCode::F10)),
                (KeycodeType::Keyboard(KeyCode::F11)),
                (KeycodeType::Keyboard(KeyCode::F12)),
                (KeycodeType::Keyboard(KeyCode::F13)),
                (KeycodeType::Keyboard(KeyCode::F14)),
                (KeycodeType::Keyboard(KeyCode::F15)),
                (KeycodeType::Keyboard(KeyCode::F16)),
                (KeycodeType::Keyboard(KeyCode::F17)),
                (KeycodeType::Keyboard(KeyCode::F18)),
                (KeycodeType::Keyboard(KeyCode::F19)),
                (KeycodeType::Keyboard(KeyCode::F20)),
                (KeycodeType::Keyboard(KeyCode::F21)),
                (KeycodeType::Keyboard(KeyCode::F22)),
                (KeycodeType::Keyboard(KeyCode::F23)),
                (KeycodeType::Keyboard(KeyCode::F24)),
                (KeycodeType::Keyboard(KeyCode::Insert)),
                (KeycodeType::Keyboard(KeyCode::Home)),
                (KeycodeType::Keyboard(KeyCode::Delete)),
                (KeycodeType::Keyboard(KeyCode::End)),
                (KeycodeType::Keyboard(KeyCode::PageDown)),
                (KeycodeType::Keyboard(KeyCode::PageUp)),
                (KeycodeType::Keyboard(KeyCode::Left)),
                (KeycodeType::Keyboard(KeyCode::Up)),
                (KeycodeType::Keyboard(KeyCode::Right)),
                (KeycodeType::Keyboard(KeyCode::Down)),
                (KeycodeType::Keyboard(KeyCode::Back)),
                (KeycodeType::Keyboard(KeyCode::Return)),
                (KeycodeType::Keyboard(KeyCode::Space)),
                (KeycodeType::Keyboard(KeyCode::Compose)),
                (KeycodeType::Keyboard(KeyCode::Caret)),
                (KeycodeType::Keyboard(KeyCode::Numlock)),
                (KeycodeType::Keyboard(KeyCode::Numpad0)),
                (KeycodeType::Keyboard(KeyCode::Numpad1)),
                (KeycodeType::Keyboard(KeyCode::Numpad2)),
                (KeycodeType::Keyboard(KeyCode::Numpad3)),
                (KeycodeType::Keyboard(KeyCode::Numpad4)),
                (KeycodeType::Keyboard(KeyCode::Numpad5)),
                (KeycodeType::Keyboard(KeyCode::Numpad6)),
                (KeycodeType::Keyboard(KeyCode::Numpad7)),
                (KeycodeType::Keyboard(KeyCode::Numpad8)),
                (KeycodeType::Keyboard(KeyCode::Numpad9)),
                (KeycodeType::Keyboard(KeyCode::NumpadAdd)),
                (KeycodeType::Keyboard(KeyCode::NumpadDivide)),
                (KeycodeType::Keyboard(KeyCode::NumpadDecimal)),
                (KeycodeType::Keyboard(KeyCode::NumpadComma)),
                (KeycodeType::Keyboard(KeyCode::NumpadEnter)),
                (KeycodeType::Keyboard(KeyCode::NumpadEquals)),
                (KeycodeType::Keyboard(KeyCode::NumpadMultiply)),
                (KeycodeType::Keyboard(KeyCode::NumpadSubtract)),
                (KeycodeType::Keyboard(KeyCode::Backslash)),
                (KeycodeType::Keyboard(KeyCode::Equals)),
                (KeycodeType::Keyboard(KeyCode::LAlt)),
                (KeycodeType::Keyboard(KeyCode::LBracket)),
                (KeycodeType::Keyboard(KeyCode::LControl)),
                (KeycodeType::Keyboard(KeyCode::LShift)),
                (KeycodeType::Keyboard(KeyCode::LWin)),
                (KeycodeType::Keyboard(KeyCode::Minus)),
                (KeycodeType::Keyboard(KeyCode::Period)),
                (KeycodeType::Keyboard(KeyCode::RAlt)),
                (KeycodeType::Keyboard(KeyCode::RShift)),
                (KeycodeType::Keyboard(KeyCode::RWin)),
                (KeycodeType::Keyboard(KeyCode::Semicolon)),
                (KeycodeType::Keyboard(KeyCode::Slash)),
                (KeycodeType::Keyboard(KeyCode::Tab)),
                // (KeyTypes::Gamepad(Button::)),
            ];

            for keytype in keyvalue_pairs {
                hash_map.insert(
                    keytype,
                    Key {
                        keycode: StringifiableKeyCode(keytype),
                        name: keycode_converter::keycode_to_str(keytype)
                            .expect("keytype is invalid"),
                        status: KeyStatus::default(),
                        event_occured: false,
                    },
                );
            }
        };

        hash_map
    })
}
