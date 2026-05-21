package com.iamomnishropbot.opndoc.ui.wave

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.RepeatMode
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Path
import kotlin.math.PI
import kotlin.math.sin

/**
 * Animated Gemini-style background.
 *
 * The provided colors are blended in gradients across three wave layers.
 * Updates are immediate whenever new colors are provided.
 */
@Composable
fun WaveBackground(
    colors: List<Color>,
    modifier: Modifier = Modifier
) {
    val safeColors = if (colors.size >= 3) colors else listOf(
        Color(0xFF6C63FF), Color(0xFF00C2FF), Color(0xFFFF5EAE)
    )

    val transition = rememberInfiniteTransition(label = "wave-transition")
    val phase by transition.animateFloat(
        initialValue = 0f,
        targetValue = (2f * PI).toFloat(),
        animationSpec = infiniteRepeatable(
            animation = tween(durationMillis = 7000, easing = LinearEasing),
            repeatMode = RepeatMode.Restart
        ),
        label = "wave-phase"
    )

    Canvas(modifier = modifier.fillMaxSize()) {
        val width = size.width
        val height = size.height

        drawRect(
            brush = Brush.linearGradient(
                colors = listOf(
                    safeColors[0].copy(alpha = 0.75f),
                    safeColors[1].copy(alpha = 0.68f),
                    safeColors[2].copy(alpha = 0.75f)
                ),
                start = Offset.Zero,
                end = Offset(width, height)
            )
        )

        repeat(3) { layer ->
            val amplitude = (24f + (layer * 20f))
            val baseline = height * (0.42f + (layer * 0.14f))
            val wavelength = width / (1.25f + (layer * 0.15f))
            val alpha = 0.34f + (layer * 0.11f)

            val path = Path().apply {
                moveTo(0f, height)
                lineTo(0f, baseline)
                var x = 0f
                while (x <= width) {
                    val angle = ((x / wavelength) * 2f * PI + phase + layer).toDouble()
                    val y = baseline + amplitude * sin(angle).toFloat()
                    lineTo(x, y)
                    x += 6f
                }
                lineTo(width, height)
                close()
            }

            drawPath(
                path = path,
                brush = Brush.horizontalGradient(
                    colors = listOf(
                        safeColors[layer % 3].copy(alpha = alpha),
                        safeColors[(layer + 1) % 3].copy(alpha = alpha),
                        safeColors[(layer + 2) % 3].copy(alpha = alpha)
                    ),
                    startX = 0f,
                    endX = width
                )
            )
        }
    }
}
