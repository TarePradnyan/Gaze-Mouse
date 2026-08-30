# Gaze-Mouse

Eye-gaze tracking system using MediaPipe that enables mouse control  interaction through facial landmarks and eye detection.

## Overview

Gaze-Mouse is a Python-based computer vision project that leverages MediaPipe's FaceMesh to detect facial landmarks and iris positions in real-time. This enables hands-free interaction with your computer through:

- **Eye gaze tracking** for mouse cursor movement
- **Blink detection** for mouse clicks


## Features

###  Core Functionality

- **Eye Tracking**: Real-time iris detection to track eye position and convert it to screen coordinates
- **Blink Detection**: Automatically detects eye blinks to trigger mouse clicks or keyboard input
- **Face Mesh Visualization**: Display facial landmarks and mesh connections for debugging and visualization

###  Supported Interactions

- Mouse cursor movement based on iris position
- Click detection through eye blinks
## Requirements

### Dependencies

- Python 3.7+
- OpenCV (cv2)
- MediaPipe
- PyAutoGUI

### Installation

1. Clone the repository:
```bash
git clone https://github.com/TarePradnyan/Gaze-Mouse.git
cd Gaze-Mouse
python main.py
