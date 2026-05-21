package com.iamomnishropbot.opndoc.ui.wave

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp

/**
 * Dependency-free color picker dialog.
 *
 * Uses a curated palette to keep combinations vivid and harmonious across devices.
 */
@Composable
fun WaveColorPickerDialog(
    title: String,
    currentColor: Color,
    onDismiss: () -> Unit,
    onColorPicked: (Color) -> Unit
) {
    val palette = listOf(
        Color(0xFF6C63FF), Color(0xFF00C2FF), Color(0xFFFF5EAE), Color(0xFFFFA751),
        Color(0xFF52E5A3), Color(0xFF8E2DE2), Color(0xFF00B09B), Color(0xFFE94057),
        Color(0xFF4E54C8), Color(0xFF24C6DC), Color(0xFFF857A6), Color(0xFF43CEA2)
    )

    AlertDialog(
        onDismissRequest = onDismiss,
        title = { Text(text = title) },
        text = {
            androidx.compose.foundation.layout.Column {
                palette.chunked(4).forEach { rowColors ->
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceEvenly,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        rowColors.forEach { color ->
                            val isSelected = color == currentColor
                            Box(
                                modifier = Modifier
                                    .size(48.dp)
                                    .clip(CircleShape)
                                    .background(color)
                                    .border(
                                        width = if (isSelected) 3.dp else 1.dp,
                                        color = if (isSelected) MaterialTheme.colorScheme.onSurface else Color.White.copy(alpha = 0.6f),
                                        shape = CircleShape
                                    )
                                    .clickable { onColorPicked(color) }
                            )
                        }
                    }
                    Spacer(modifier = Modifier.height(12.dp))
                }
            }
        },
        confirmButton = {
            TextButton(onClick = onDismiss) {
                Text(text = "Done")
            }
        },
        modifier = Modifier.padding(horizontal = 8.dp)
    )
}
