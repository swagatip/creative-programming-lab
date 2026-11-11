"""
Perlin Noise Flow Field (Vectorized)
A generative art sketch built with py5 and NumPy.

Inspired by classic creative coding flow field techniques (Daniel Shiffman's
"The Nature of Code" and Tyler Hobbs' "Flow Fields").
Initial boilerplate generated with AI assistance and customized by [Your Name].
"""


import py5
import numpy as np
from datetime import datetime

import py5_tools

# Sketch & Canvas Configuration
WIDTH: int = 800
HEIGHT: int = 800
BG_COLOR: tuple[int, int, int] = (15, 18, 25)
TRAIL_FADE_ALPHA: int = 8

# Flow Field & Particle Parameters
NUM_PARTICLES: int = 10000
NOISE_SCALE: float = 0.005
TIME_SPEED: float = 0.002
CURL_FACTOR: float = 2.0
STEP_LENGTH: float = 2.0

# Visual Styling
STROKE_COLOR: tuple[int, int, int, int] = (100, 220, 255, 45)
STROKE_WEIGHT: float = 1.0

# Global State
particles: np.ndarray


def setup() -> None:
    """Initialize the canvas and spawn particles uniformly across the screen."""
    py5.size(WIDTH, HEIGHT)
    py5.background(*BG_COLOR)

    global particles
    rng = np.random.default_rng()
    particles = rng.random((NUM_PARTICLES, 2)) * np.array([py5.width, py5.height])


def draw() -> None:
    """Update all particle positions simultaneously and render line segments."""
    global particles

    # Apply subtle translucent overlay for fading trails
    py5.no_stroke()
    py5.fill(*BG_COLOR, TRAIL_FADE_ALPHA)
    py5.rect(0, 0, py5.width, py5.height)

    # Sample 3D Perlin noise across all (x, y) coordinates in one vectorized call
    noise_vals = py5.noise(
        particles[:, 0] * NOISE_SCALE,
        particles[:, 1] * NOISE_SCALE,
        py5.frame_count * TIME_SPEED,
    )
    angles = noise_vals * py5.TWO_PI * CURL_FACTOR

    # Compute next positions via vectorized trigonometry
    dx = np.cos(angles) * STEP_LENGTH
    dy = np.sin(angles) * STEP_LENGTH
    next_particles = particles + np.column_stack((dx, dy))

    # Batch-draw all segments in a single call: shape (N, 4) -> [x1, y1, x2, y2]
    py5.stroke(*STROKE_COLOR)
    py5.stroke_weight(STROKE_WEIGHT)
    segments = np.hstack((particles, next_particles))
    py5.lines(segments)

    # Wrap particles around screen boundaries
    particles = next_particles % np.array([py5.width, py5.height])


def key_pressed() -> None:
    """
    Save a high-resolution PNG snapshot when 's' is pressed.
    Save a GIF when 'g' is pressed'
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if py5.key == "s":
        
        py5.save_frame(f"outputs/flow_art_perlin_noise{timestamp}_####.png")
    elif py5.key == "g":
        print("Recording GIF...")
        py5_tools.animated_gif(
            f"outputs/flow_art_perlin_noise_{timestamp}.gif",
            count=120,       # Total number of frames to capture
            period=0.033,    # Seconds between frames (~30 FPS)
            duration=0.033,  # Playback delay per frame in the final GIF
        )


if __name__ == "__main__":
    py5.run_sketch()
