import cv2
import mediapipe as mp
from handtrackingmodule import  HandDetector
import pyautogui as py


detector=HandDetector()



capture =cv2.VideoCapture(0)

while True:
    sucess,img=capture.read()
    lmlist,img=detector.lmlist(img)
    
    if lmlist:
        fingers,img=detector.fingersup(img,lmlist)

        
        if(fingers==[0,0,0,0,0]):
            py.scroll(-50)
        elif(fingers==[1,1,1,1,1]):
            py.scroll(50)

        #print(fingers)

    cv2.imshow("video feed",img)
    key=cv2.waitKey(1)
    if(key==27):
        break


capture.release()
cv2.destroyAllWindows()

