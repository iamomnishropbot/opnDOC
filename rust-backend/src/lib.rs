use jni::objects::{JClass, JString};
use jni::sys::jstring;
use jni::JNIEnv;
use serde::{Serialize, Deserialize};
use std::collections::HashMap;

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
    let json: String = env
        .get_string(&json_input)
        .expect("Couldn't get string!")
        .into();
    let brain: BrainData = serde_json::from_str(&json).unwrap_or_default();
    let result_json = serde_json::to_string(&brain).expect("Serialization failed!");
    env.new_string(result_json).unwrap().into_raw()
}
