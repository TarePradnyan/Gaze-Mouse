


import cv2
import mediapipe as mp
import pyautogui as pg
from main import Blink

class FaceMeshDetector():
  def __init__(self, staticMode=False, maxFaces= 1, minDetectionCon=0.5,minTrackCon=0.5):
    self.staticMode = staticMode
    self.maxFaces = maxFaces
    self.minDetectionCon = minDetectionCon
    self.minTrackCon = minTrackCon
    self.y1 = 0
    
    
    
    
    
     
    # mpDraw = mp.solutions.drawing_utils
    self.mpFaceMesh = mp.solutions.face_mesh
    self.faceMesh = self.mpFaceMesh.FaceMesh()
  def FindFaceMesh(self, img,times):
    self.imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    self.results = self.faceMesh.process(self.imgRGB)
    
    if self.results.multi_face_landmarks:
      for faceLms in  self.results.multi_face_landmarks:
        # self.mpDraw.draw_landmarks(img,faceLms)
        for id, lm in enumerate(faceLms.landmark):
          # print(lm)
          ih,iw,ic = img.shape
          # print(ih,iw,ic)
          if id == 226:
            x226= int(lm.x*iw)
            
          if id == 263:
              x263= int(lm.x*iw)
            
            
          if id == 8:
            x8 = int(lm.x*iw)
          if id == 10:
            
            x10 = int(lm.x*iw)
          if id == 1:
            if times == 0:
              x1 = 0
              self.y1 = 0
              self.oldY = 0
            self.oldY = self.y1
            
            x1 = int(lm.x*iw)
            self.y1 = int(lm.y*ih)
            oldY = self.oldY
            y1 = self.y1
            diff = y1- self.oldY

            

            #   cv2.circle(img,(x,y),3,(255,0,0),3)
            # cv2.putText(img, str(id),(x,y),cv2.FONT_HERSHEY_PLAIN,0.5,(0,255,0),thickness=1)
        if bool(x8) or bool(x263) or bool(x226) !=False :
          look=""
          PosX = pg.position()[0]  #a
          PosYp = pg.position()[1]  #b
          
          
          # print(f"distance between 8 and 263 is {x8-x263}, distance between 8 and 226 is {x226-x8} distance between down 8 and 10 is {x10-x8}, distance between 8 and 1 is {x8-x1}")  
          if  x8-x263 > -40:
            look = "left"
            PosX -= 10
            # PosYp +=10
            # cv2.putText(img, look, (70,90),cv2.FONT_ITALIC,3,(255,0,0),thickness=2)
            
          elif x226-x8 >-55:
            look="right"
            PosX += 10
            # PosYp-=10
            # cv2.putText(img,look, (70,90),cv2.FONT_ITALIC,3,(255,0,0),thickness=2)
          
          elif x8-x1 < 0:
            look="up"
            PosYp -= 10
            # cv2.putText(img,look, (70,90),cv2.FONT_ITALIC,3,(255,0,0),thickness=2)

          elif x8-x1> 2:
            PosYp += 10
            look="down"
            # cv2.putText(img,look, (70,90),cv2.FONT_ITALIC,3,(255,0,0),thickness=2)

          else:
            look="forward"
            # cv2.putText(img,look, (70,90),cv2.FONT_ITALIC,3,(255,0,0),thickness=2)

          # if bool(PosYn) == True:
          pg.moveTo(PosX,PosYp)

          
    
        else:
          pass
    return img

times = 0

if __name__ == "__main__":  
  cap = cv2.VideoCapture(0)
  detector = FaceMeshDetector()
  times = 0
  while True:
    success,img =  cap.read()
    img = detector.FindFaceMesh(img,times)

    img =  cv2.flip(img,1)
    Blink(img)
    cv2.imshow("Camera",img)
    
    if cv2.waitKey(1) == 27:
      break
    

    times=times+1
  cv2.destroyAllWindows()