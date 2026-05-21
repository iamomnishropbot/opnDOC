use jni::objects::{JClass, JString};
use jni::sys::jstring;
use jni::JNIEnv;
use serde::{Serialize, Deserialize};
use std::collections::HashMap;
use std::ptr::null_mut;

#[derive(Serialize, Deserialize)]
pub struct BrainData {
    pub word_fix: HashMap<String, String>,
    pub history_log: Vec<String>,
    pub user_profile: HashMap<String, String>,
}

impl Default for BrainData {
    fn default() -> Self {
        BrainData {
            word_fix: HashMap::new(),
            history_log: Vec::new(),
            user_profile: HashMap::new(),
        }
    }
}

#[no_mangle]
pub extern "C" fn Java_com_iamomnishropbot_opndoc_BrainDataBridge_parseFromJson(
    mut env: JNIEnv,
    _class: JClass,
    json_input: JString,
) -> jstring {
    let json: String = match env.get_string(&json_input) {
        Ok(value) => value.into(),
        Err(error) => {
            let _ = env.throw_new(
                "java/lang/IllegalArgumentException",
                format!("Failed to read input JSON string: {error}"),
            );
            return null_mut();
        }
    };
    let brain: BrainData = serde_json::from_str(&json).unwrap_or_default();
    let result_json = match serde_json::to_string(&brain) {
        Ok(value) => value,
        Err(error) => {
            let _ = env.throw_new(
                "java/lang/RuntimeException",
                format!("Failed to serialize normalized brain data: {error}"),
            );
            return null_mut();
        }
    };

    match env.new_string(result_json) {
        Ok(value) => value.into_raw(),
        Err(error) => {
            let _ = env.throw_new(
                "java/lang/RuntimeException",
                format!("Failed to allocate JNI output string: {error}"),
            );
            null_mut()
        }
    }
}
