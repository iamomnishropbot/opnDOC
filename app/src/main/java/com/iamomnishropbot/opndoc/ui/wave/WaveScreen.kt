package com.iamomnishropbot.opndoc.ui.wave

import android.content.res.ColorStateList
import android.view.ContextThemeWrapper
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.toArgb
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.unit.dp
import androidx.compose.ui.viewinterop.AndroidView
import androidx.lifecycle.viewmodel.compose.viewModel
import com.google.android.material.button.MaterialButton

/**
 * Entry composable for the dynamic Gemini-style wave screen.
 *
 * Integration notes:
 * 1) Set this composable as your screen content inside your existing navigation graph.
 * 2) Replace the logo placeholder block with your own painterResource image.
 * 3) Wire `onTestClick` to your real navigation/action handler.
 */
@Composable
fun WaveScreen(
    viewModel: WaveViewModel = viewModel(),
    onTestClick: (List<Color>) -> Unit = {}
) {
    val uiState by viewModel.uiState.collectAsState()
    var pickerIndex by remember { mutableIntStateOf(-1) }

    Box(modifier = Modifier.fillMaxSize()) {
        WaveBackground(
            colors = uiState.selectedColors,
            modifier = Modifier.fillMaxSize()
        )

        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(20.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Top
        ) {
            Spacer(modifier = Modifier.height(20.dp))

            Box(
                modifier = Modifier
                    .size(width = 180.dp, height = 72.dp)
                    .clip(RoundedCornerShape(20.dp))
                    .background(Color.White.copy(alpha = 0.22f)),
                contentAlignment = Alignment.Center
            ) {
                // Replace this placeholder with your logo asset when available, for example:
                // Image(
                //     painter = painterResource(id = R.drawable.your_logo),
                //     contentDescription = "App logo",
                //     modifier = Modifier.fillMaxSize().padding(8.dp)
                // )
                Text(
                    text = "Logo Placeholder",
                    color = Color.White,
                    style = MaterialTheme.typography.titleMedium
                )
            }

            Spacer(modifier = Modifier.height(28.dp))

            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceEvenly
            ) {
                uiState.selectedColors.forEachIndexed { index, color ->
                    Button(
                        modifier = Modifier.semantics {
                            contentDescription = "Pick Color ${index + 1} button"
                        },
                        onClick = { pickerIndex = index },
                        colors = ButtonDefaults.buttonColors(
                            containerColor = color,
                            contentColor = color.contrastText()
                        )
                    ) {
                        Text(text = "Pick Color ${index + 1}")
                    }
                }
            }

            Spacer(modifier = Modifier.height(22.dp))

            HarmonizedMaterialTestButton(
                colors = uiState.selectedColors,
                onClick = { onTestClick(uiState.selectedColors) }
            )

            Spacer(modifier = Modifier.height(10.dp))

            Text(
                text = "Tip: Hook onTestClick to navigate or trigger app actions.",
                color = Color.White.copy(alpha = 0.92f),
                style = MaterialTheme.typography.bodyMedium
            )
        }
    }

    if (pickerIndex >= 0) {
        WaveColorPickerDialog(
            title = "Pick Color ${pickerIndex + 1}",
            currentColor = uiState.selectedColors[pickerIndex],
            onDismiss = { pickerIndex = -1 },
            onColorPicked = { selected ->
                viewModel.updateColor(pickerIndex, selected)
                pickerIndex = -1
            }
        )
    }
}

/**
 * Example traditional MaterialButton wrapped inside Compose.
 *
 * Keeps compatibility with existing View-based button styling while still living in Compose.
 */
@Composable
private fun HarmonizedMaterialTestButton(
    colors: List<Color>,
    onClick: () -> Unit
) {
    val harmonized = blend(colors)
    val textColor = harmonized.contrastText()

    AndroidView(
        modifier = Modifier
            .fillMaxWidth(0.62f)
            .height(52.dp),
        factory = { ctx ->
            MaterialButton(
                ContextThemeWrapper(
                    ctx,
                    com.google.android.material.R.style.Theme_MaterialComponents_DayNight
                )
            ).apply {
                text = "Test"
                cornerRadius = (28 * ctx.resources.displayMetrics.density).toInt()
                setOnClickListener { onClick() }
            }
        },
        update = { button ->
            button.backgroundTintList = ColorStateList.valueOf(harmonized.toArgb())
            button.setTextColor(textColor.toArgb())
        }
    )
}

private fun blend(colors: List<Color>): Color {
    val safe = if (colors.size >= 3) colors else DefaultWaveColors
    return Color(
        red = (safe[0].red + safe[1].red + safe[2].red) / 3f,
        green = (safe[0].green + safe[1].green + safe[2].green) / 3f,
        blue = (safe[0].blue + safe[1].blue + safe[2].blue) / 3f,
        alpha = 1f
    )
}

private fun Color.contrastText(): Color {
    val luma = (0.299f * red) + (0.587f * green) + (0.114f * blue)
    return if (luma > 0.6f) Color.Black else Color.White
}
