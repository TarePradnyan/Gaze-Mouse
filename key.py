# import the opencv library
import cv2
import pyautogui
import mediapipe as mp
  
from time import sleep
font = cv2.FONT_HERSHEY_TRIPLEX
def box(resized):
    # First Line

    cv2.rectangle(resized,(40,10),(140,110),(255,0,0),3)################### P
    cv2.rectangle(resized,(150,10),(250,110),(255,0,0),3)################## O
    cv2.rectangle(resized,(260,10),(360,110),(255,0,0),3)################## I
    cv2.rectangle(resized,(370,10),(470,110),(255,0,0),3)################## U
    cv2.rectangle(resized,(480,10),(580,110),(255,0,0),3)################## Y
    cv2.rectangle(resized,(590,10),(690,110),(255,0,0),3)################## T
    cv2.rectangle(resized,(700,10),(800,110),(255,0,0),3)################## R
    cv2.rectangle(resized,(810,10),(910,110),(255,0,0),3)################## E
    cv2.rectangle(resized,(920,10),(1020,110),(255,0,0),3)################# W
    cv2.rectangle(resized,(1030,10),(1130,110),(255,0,0),3)################ Q


    # secongd Line
    cv2.rectangle(resized,(980,120),(1080,220),(255,0,0),3)################ L
    cv2.rectangle(resized,(870,120),(970,220),(255,0,0),3)################# K
    cv2.rectangle(resized,(760,120),(860,220),(255,0,0),3)################# J
    cv2.rectangle(resized,(650,120),(750,220),(255,0,0),3)################# H
    cv2.rectangle(resized,(540,120),(640,220),(255,0,0),3)################# G
    cv2.rectangle(resized,(430,120),(530,220),(255,0,0),3)################# F
    cv2.rectangle(resized,(320,120),(420,220),(255,0,0),3)################# D
    cv2.rectangle(resized,(210,120),(310,220),(255,0,0),3)################# S
    cv2.rectangle(resized,(100,120),(200,220),(255,0,0),3)################# A
    
    # Third Line
    cv2.rectangle(resized,(870,230),(970,330),(255,0,0),3)################# M
    cv2.rectangle(resized,(760,230),(860,330),(255,0,0),3)################# N
    cv2.rectangle(resized,(650,230),(750,330),(255,0,0),3)################# B
    cv2.rectangle(resized,(540,230),(640,330),(255,0,0),3)################# V
    cv2.rectangle(resized,(430,230),(530,330),(255,0,0),3)################# C
    cv2.rectangle(resized,(320,230),(420,330),(255,0,0),3)################# X
    cv2.rectangle(resized,(210,230),(310,330),(255,0,0),3)################# Z
    

def alphabet(resized):
    
    # First Line

    P = cv2.putText(resized,"P",(70,90),font,3,(255,0,0),thickness=2)################### P (40,10),(140,110)
    O = cv2.putText(resized,"O",(170,90),font,3,(255,0,0),thickness=2)################### O
    I = cv2.putText(resized,"I",(290,90),font,3,(255,0,0),thickness=2)################### I
    U = cv2.putText(resized,"U",(390,90),font,3,(255,0,0),thickness=2)################### U
    Y = cv2.putText(resized,"Y",(490,90),font,3,(255,0,0),thickness=2)################### Y
    T = cv2.putText(resized,"T",(610,90),font,3,(255,0,0),thickness=2)################### T
    R = cv2.putText(resized,"R",(710,90),font,3,(255,0,0),thickness=2)################### R
    E = cv2.putText(resized,"E",(825,90),font,3,(255,0,0),thickness=2)################### E
    W = cv2.putText(resized,"W",(930,90),font,3,(255,0,0),thickness=2)################### W
    Q = cv2.putText(resized,"Q",(1050,90),font,3,(255,0,0),thickness=2)################### Q

    # Second Line

    L = cv2.putText(resized,"L",(120,200),font,3,(255,0,0),thickness=2)#################### L 
    K = cv2.putText(resized,"K",(220,200),font,3,(255,0,0),thickness=2)################### K
    J = cv2.putText(resized,"J",(340,200),font,3,(255,0,0),thickness=2)################### J
    H = cv2.putText(resized,"H",(445,200),font,3,(255,0,0),thickness=2)################### H
    G = cv2.putText(resized,"G",(550,200),font,3,(255,0,0),thickness=2)################### G
    F = cv2.putText(resized,"F",(670,200),font,3,(255,0,0),thickness=2)################### F
    D = cv2.putText(resized,"D",(770,200),font,3,(255,0,0),thickness=2)################### D
    S = cv2.putText(resized,"S",(890,200),font,3,(255,0,0),thickness=2)################### S
    A = cv2.putText(resized,"A",(1000,200),font,3,(255,0,0),thickness=2)################## A

    # third line
    M = cv2.putText(resized,"M",(230,310),font,3,(255,0,0),thickness=2)################### M
    N = cv2.putText(resized,"N",(345,310),font,3,(255,0,0),thickness=2)################### N
    B = cv2.putText(resized,"B",(450,310),font,3,(255,0,0),thickness=2)################### B
    V = cv2.putText(resized,"V",(570,310),font,3,(255,0,0),thickness=2)################### V
    C = cv2.putText(resized,"C",(670,310),font,3,(255,0,0),thickness=2)################### C
    X = cv2.putText(resized,"X",(790,310),font,3,(255,0,0),thickness=2)################### X
    Z = cv2.putText(resized,"Z",(900,310),font,3,(255,0,0),thickness=2)################## Z

def Key_press(cox,coy,coz):
    x= cox
    y = coy
    z =coz
    print(x,y,z)
    # First Line
    if 30 < x < 70 and 10<y<60  and z<-7: 
        pyautogui.press("P")
        # sleep(1)
    elif 80 < x<130 and 10<y<60 and z<-7:#80,60 130,10
        pyautogui.press("O")
    elif 140 < x<190 and 10<y<60 and z<-7:  
        pyautogui.press("I")
    elif 200 < x<270 and 10<y<60 and z<-7:  
         pyautogui.press("U")
    elif 260 < x<300 and 10<y<60 and z<-7:  
       pyautogui.press("Y")
    elif 315 < x<365 and 10<y<60 and z<-7:  
        pyautogui.press("T")
    elif 375 < x<430 and 10<y<60 and z<-7:
        pyautogui.press("R")
    elif  430< x<480 and 10<y<60 and z<-7:
        pyautogui.press("E")
    elif 495 < x<540 and 10<y<60 and z<-7:
        pyautogui.press("W")
    elif 555 < x<600 and 10<y<60 and z<-7:
        pyautogui.press("Q")


    #     # Second Line
    elif 50 < x<100 and 70<y<120 and z<-7:
        pyautogui.press("L")
    elif 115 < x<165 and 70<y<120 and z<-7:
        pyautogui.press("K")
    elif 175 < x<220 and 70<y<120 and z<-7:
        pyautogui.press("J")
    elif 235 < x<275 and 70<y<120 and z<-7:
        pyautogui.press("H")
    elif 290 < x<335 and 70<y<120 and z<-7:
        pyautogui.press("G")
    elif 350 < x<395 and 70<y<120 and z<-7:
        pyautogui.press("F")
    elif 410 < x<455 and 70<y<120 and z<-7:
        pyautogui.press("D")
    elif 470 < x<515 and 70<y<120 and z<-7:
        pyautogui.press("S")
    elif 530 < x<570 and 70<y<120 and z<-7:
        pyautogui.press("A")
    
    #     # Third Line
    
    elif 115 < x<165 and 138<y<200 and z<-7:
        pyautogui.press("M")
    elif 175 < x<220 and 138<y<200 and z<-7:
        pyautogui.press("N")
    elif 234 < x<280 and 138<y<200 and z<-7:
        pyautogui.press("B")
    elif 290 < x<335 and 138<y<200 and z<-7:
        pyautogui.press("V")
    elif 350 < x<395 and 138<y<200 and z<-7:
        pyautogui.press("C")
    elif 410 < x<460 and 138<y<200 and z<-7:
        pyautogui.press("X")
    elif 465 < x<515 and 138<y<200 and z<-7:
        pyautogui.press("Z")
def alphabet(resized):
    
    # First Line

    P = cv2.putText(resized,"P",(70,90),font,3,(255,0,0),thickness=2)################### P (40,10),(140,110)
    O = cv2.putText(resized,"O",(170,90),font,3,(255,0,0),thickness=2)################### O
    I = cv2.putText(resized,"I",(290,90),font,3,(255,0,0),thickness=2)################### I
    U = cv2.putText(resized,"U",(390,90),font,3,(255,0,0),thickness=2)################### U
    Y = cv2.putText(resized,"Y",(490,90),font,3,(255,0,0),thickness=2)################### Y
    T = cv2.putText(resized,"T",(610,90),font,3,(255,0,0),thickness=2)################### T
    R = cv2.putText(resized,"R",(710,90),font,3,(255,0,0),thickness=2)################### R
    E = cv2.putText(resized,"E",(825,90),font,3,(255,0,0),thickness=2)################### E
    W = cv2.putText(resized,"W",(930,90),font,3,(255,0,0),thickness=2)################### W
    Q = cv2.putText(resized,"Q",(1050,90),font,3,(255,0,0),thickness=2)################### Q

    # Second Line

    L = cv2.putText(resized,"L",(120,200),font,3,(255,0,0),thickness=2)#################### L 
    K = cv2.putText(resized,"K",(220,200),font,3,(255,0,0),thickness=2)################### K
    J = cv2.putText(resized,"J",(340,200),font,3,(255,0,0),thickness=2)################### J
    H = cv2.putText(resized,"H",(445,200),font,3,(255,0,0),thickness=2)################### H
    G = cv2.putText(resized,"G",(550,200),font,3,(255,0,0),thickness=2)################### G
    F = cv2.putText(resized,"F",(670,200),font,3,(255,0,0),thickness=2)################### F
    D = cv2.putText(resized,"D",(770,200),font,3,(255,0,0),thickness=2)################### D
    S = cv2.putText(resized,"S",(890,200),font,3,(255,0,0),thickness=2)################### S
    A = cv2.putText(resized,"A",(1000,200),font,3,(255,0,0),thickness=2)################## A

    # third line
    M = cv2.putText(resized,"M",(230,310),font,3,(255,0,0),thickness=2)################### M
    N = cv2.putText(resized,"N",(345,310),font,3,(255,0,0),thickness=2)################### N
    B = cv2.putText(resized,"B",(450,310),font,3,(255,0,0),thickness=2)################### B
    V = cv2.putText(resized,"V",(570,310),font,3,(255,0,0),thickness=2)################### V
    C = cv2.putText(resized,"C",(670,310),font,3,(255,0,0),thickness=2)################### C
    X = cv2.putText(resized,"X",(790,310),font,3,(255,0,0),thickness=2)################### X
    Z = cv2.putText(resized,"Z",(900,310),font,3,(255,0,0),thickness=2)################## Z 900,310


# define a video capture object
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
while(True):


    _, frame = cam.read()
    resized = cv2.resize(frame,(1200,815))
    frame = cv2.flip(frame, 1)
    resized= cv2.flip(resized, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
            # print(left[0].y - left[1].y)
        if (left[0].y - left[1].y) < 0.021:
            pyautogui.click()
            pyautogui.sleep(1)
    keyboard = cv2.putText(resized,"keyboard",(100,180),font,3,(255,0,0),thickness=2)################### N
    cv2.rectangle(resized,(90,90),(650,200),(255,0,0),3)################# Z
    print(pyautogui.position())
    if 100<=pyautogui.position()[0]<= 650 and 100 <= pyautogui.position()[1] <= 200:
        
        alphabet(resized)
        box(resized)
    
    cv2.imshow('resized', resized)
      

    if cv2.waitKey(1) == 27:
        break
  

cam.release()

cv2.destroyAllWindows()