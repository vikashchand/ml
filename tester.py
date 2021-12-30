import cv2
import mediapipe as mp
from handtrackingmodule import  HandDetector


detector=HandDetector()



mpHands =mp.solutions.hands
hands=mpHands.Hands()
drawTools =mp.solutions.drawing_utils
capture =cv2.VideoCapture(0)

while True:
    sucess,img=capture.read()
    lmlist,img=detector.lmlist(img)
    print(lmlist)

    cv2.imshow("video feed",img)
    key=cv2.waitKey(1)
    if(key==27):
        break


capture.release()
cv2.destroyAllWindows()

