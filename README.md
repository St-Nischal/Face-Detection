# Face Detection with OpenCV and MediaPipe-silicon

This is a basic real-time face detection script using your webcam. It uses [MediaPipe](https://github.com/google/mediapipe) for face detection and [OpenCV](https://opencv.org/) for image processing and display.

## 🛠️ Requirements

Make sure you have the following Python packages installed:

```bash
pip install opencv-python mediapipe

📸 How It Works

    Captures video from your webcam (cv2.VideoCapture(0))

    Uses MediaPipe's face detection model to detect faces in real-time

    Draws bounding boxes around detected faces

    Displays the frame rate (FPS) on the screen

🚀 Running the Script

python face_detection.py

Press q to quit the video window.
📄 Output

    Face bounding boxes are drawn directly onto the video feed

    Console logs show the relative bounding box data for each detection

    FPS is displayed in the top-left corner

📁 File Overview

    face_detection.py: The main script

    No additional resources are needed — runs directly from webcam input

🧼 Exit and Cleanup

The script cleanly releases the webcam and destroys all OpenCV windows when q is pressed.
