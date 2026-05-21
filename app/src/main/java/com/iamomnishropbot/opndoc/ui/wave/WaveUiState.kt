package com.iamomnishropbot.opndoc.ui.wave

import androidx.compose.ui.graphics.Color

/**
 * UI state for the Gemini-style wave screen.
 *
 * Replace the default colors with persisted values if/when you wire this to app storage.
 */
data class WaveUiState(
    val selectedColors: List<Color> = listOf(
        Color(0xFF6C63FF),
        Color(0xFF00C2FF),
        Color(0xFFFF5EAE)
    )
)
