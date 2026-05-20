package com.iamomnishropbot.opndoc

import android.content.Context
import org.json.JSONObject
import java.io.File

class BrainDataBridge(private val context: Context) {

    companion object {
        init {
            System.loadLibrary("rust_backend") // Must match Rust crate name
        }
    }

    // JNI bridge
    private external fun parseFromJson(json: String): String

    private val filename = "realai_brain.json"

    fun saveBrainData(data: Map<String, Any>) {
        val jsonString = JSONObject(data).toString(4)
        val file = File(context.filesDir, filename)
        file.writeText(jsonString)
    }

    fun loadBrainData(): Map<String, Any> {
        val file = File(context.filesDir, filename)
        val jsonString = if (file.exists()) file.readText() else defaultBrainJson()
        val normalizedJson = parseFromJson(jsonString)
        return JSONObject(normalizedJson).toMap()
    }

    private fun defaultBrainJson() = """
        {
            "word_fix": {},
            "history_log": [],
            "user_profile": {}
        }
        """.trimIndent()

    private fun JSONObject.toMap(): Map<String, Any> =
        keys().asSequence().associateWith { k ->
            when (val v = this[k]) {
                is JSONObject -> v.toMap()
                else -> v
            }
        }
}
