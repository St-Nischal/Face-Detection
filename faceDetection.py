import cv2
import cv2 as cv
import mediapipe as mp
import time

from fontTools.cffLib.transforms import remove_unused_subroutines

pTime = 0

#If I add 0 to video capture then it uses webcam, if I put file path to video then it uses that video
cap = cv.VideoCapture(0)

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils

faceDetection = mpFaceDetection.FaceDetection()

while True:
    success, img = cap.read()
    if not success:
        break

    #Must convert image to the right colours as Media pipe will not work without them
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)

    if results.detections:
        for id, detection in enumerate(results.detections):
            #print(id, detection)
            print(detection.location_data.relative_bounding_box)
            mpDraw.draw_detection(img,detection)

    cTime = time.time()
    fps = 1 /(cTime -pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)), (10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255), 2)

    cv.imshow("Image", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
