import cv2
import mediapipe as mp
import time

class FaceDetector():
    def __init__(self, minDetectionCon = 0.5):
        self.minDetectionCon = minDetectionCon

        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)

    def findFaces(self, img, draw = True):
        # Must convert image to the right colours as Media pipe will not work without them
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)

        boxes = []

        if self.results.detections:
            for id, detection in enumerate(self.results.detections):


                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape

                # Manually did the height, width and other corrdinates at bounding box was also encompassing the neck
                # Wanted cleaner face analysis

                x = int(bboxC.xmin * iw)
                y = int(bboxC.ymin * ih)
                w = int(bboxC.width * iw)
                h = int(bboxC.height * ih)

                bbox = (x, y, w, h)

                boxes.append([id, bbox, detection.score])

                if draw:

                    img = self.fancyDraw(img,bbox)


                    cv2.putText(img, f'FPS:{int(detection.score[0] * 100)}%',
                                (bbox[0], bbox[1] - 20),
                                cv2.FONT_HERSHEY_PLAIN,
                                3,
                                (255, 0, 255),
                                2)
        return img, boxes

    def fancyDraw(self, img, bbox, l=30, t=7, rt = 1):
        x, y, w, h = bbox
        x1, y1 = x+w, y+h

        cv2.rectangle(img, bbox, (225, 0, 255), rt)

        #Draws 2 small line in upper left corner
        cv2.line(img,(x,y), (x+l,y),(255,0,255),t)
        cv2.line(img, (x, y), (x , y+l), (255, 0, 255), t)

        # Draws 2 line in upper right corner
        cv2.line(img, (x1, y), (x1, y + l), (255, 0, 255), t)
        cv2.line(img, (x1, y), (x1 - l, y), (255, 0, 255), t)

        # Draws 2 small line in lower left corner
        cv2.line(img, (x, y1), (x + l, y1), (255, 0, 255), t)
        cv2.line(img, (x, y1), (x, y1 - l), (255, 0, 255), t)

        # Draws 2 small line in lower right corner
        cv2.line(img, (x1, y1), (x1 - l, y1), (255, 0, 255), t)
        cv2.line(img, (x1, y1), (x1, y1 - l), (255, 0, 255), t)





        return img



def main():
    pTime = 0

    # If I add 0 to video capture then it uses webcam, if I put file path to video then it uses that video
    cap = cv2.VideoCapture(0)

    detector = FaceDetector()


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



if __name__ == "__main__":
    main()