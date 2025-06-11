👁️‍🗨️ Face Detection with OpenCV and MediaPipe

A real-time face detection application using your webcam, built with MediaPipe for robust face detection and OpenCV for image processing and display. This version includes enhanced bounding box styling and improved face-only targeting (excludes the neck).
🛠️ Requirements

Install required packages:

pip install opencv-python mediapipe

📸 How It Works

    Captures video from your webcam (cv2.VideoCapture(0))

    Uses MediaPipe's Face Detection model to detect faces

    Calculates and draws customized bounding boxes (excluding neck area)

    Adds styled corner lines around each box

    Displays detection confidence (%) and FPS on the video feed

🚀 Running the Script

python face_detection.py

Press q to quit the video window.
📄 Output

    💠 Bounding boxes styled with colored corner lines

    🎯 Boxes are adjusted to focus strictly on the face region

    🧠 Detection confidence score displayed above each face

    ⚡ Real-time FPS displayed at the top-left corner

    🖥️ Console prints detection scores and bounding box info

📁 File Overview

    face_detection.py: Main script containing the FaceDetector class and execution loop

        Includes fancyDraw() for styled visual output

        findFaces() processes detections and filters regions to exclude neck

🧼 Exit and Cleanup

The script cleanly:

    Releases the webcam

    Destroys all OpenCV windows when q is pressed
