import cv2
import mediapipe as mp
import pyautogui
b= "00"
def Blink(img):
    b = "not"
    frame = cv2.flip(img, 1)
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
            
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
            # print(left[0].y - left[1].y)
        if (left[0].y - left[1].y) < 0.021:
            pyautogui.click()
            pyautogui.sleep(1)
            b = "blinked"
    return b

    
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
while True:
    
    _, frame = cam.read()
    
    b = Blink(frame)

    cv2.imshow('click-click', frame)
    if b == "blinked":
        break

    if cv2.waitKey(1)== 27:
        break
cv2.destroyAllWindows()