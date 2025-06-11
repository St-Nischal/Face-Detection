import cv2
import mediapipe as mp
import time
import faceDetectionModule as fc


pTime = 0

# If I add 0 to video capture then it uses webcam, if I put file path to video then it uses that video
cap = cv2.VideoCapture(0)

detector = fc.FaceDetector()


while True:
    success, img = cap.read()
    if not success:
        break

    img, bboxes = detector.findFaces(img)
    print(bboxes)



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
