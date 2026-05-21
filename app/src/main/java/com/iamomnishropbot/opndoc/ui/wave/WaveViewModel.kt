package com.iamomnishropbot.opndoc.ui.wave

import androidx.compose.ui.graphics.Color
import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update

/**
 * ViewModel that owns user-selected palette for the wave screen.
 *
 * Hook navigation/side effects from UI callbacks without mutating this state holder.
 */
class WaveViewModel : ViewModel() {

    private val _uiState = MutableStateFlow(WaveUiState())
    val uiState: StateFlow<WaveUiState> = _uiState.asStateFlow()

    /** Updates one of the three palette entries. Any Compose [Color] is accepted. */
    fun updateColor(index: Int, color: Color) {
        require(index in 0..2) { "Wave color index must be in range 0..2 (inclusive), but was $index" }
        _uiState.update { state ->
            val mutable = state.selectedColors.toMutableList()
            mutable[index] = color
            state.copy(selectedColors = mutable)
        }
    }
}
