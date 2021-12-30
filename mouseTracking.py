import cv2
import mediapipe as mp
import pyautogui as py
import numpy as np
from handtrackingmodule import  HandDetector


detector=HandDetector()

capture =cv2.VideoCapture(0)
clocx,clocy,plocx,plocy=0,0,0,0
smoothening=7
frameR=100

while True:
    sucess,img=capture.read()
    lmlist,img=detector.lmlist(img)
    if lmlist:
        fingers,img=detector.fingersup(img,lmlist,False)
        if(fingers[1]==1 and fingers[2]==0):
            x1,y1=lmlist[8][1:]
            cv2.rectangle(img,(frameR,frameR),(540,380),(255,0,255),3)
            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            posx=np.interp(x1,(frameR,640-frameR),(0,1920))
            posy=np.interp(x1,(frameR,480-frameR),(0,1080))

            clocx=plocx +(posx -plocx)/smoothening
            clocy=plocy +(posy -plocy)/smoothening

            py.moveTo(clocx,clocy)

            plocx=clocx
            plocy=clocy

        elif(fingers==[0,1,1,0,0]):   
            distance,img=detector.findDistance(8,12,img,lmlist)
            if (distance<35):
                py.click()
    cv2.imshow("video feed",img)
    key=cv2.waitKey(1)
    if(key==27):
        break


capture.release()
cv2.destroyAllWindows()

