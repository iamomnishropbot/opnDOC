package com.iamomnishropbot.opndoc.ui.wave

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.material3.MaterialTheme

/**
 * Optional activity host for quick integration/testing of the wave UI.
 *
 * If your app already has navigation, you can ignore this activity and use [WaveScreen]
 * directly inside your existing composable destination.
 */
class WaveDemoActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                WaveScreen(
                    onTestClick = { /* TODO: Navigate, save palette, or trigger action here. */ }
                )
            }
        }
    }
}
