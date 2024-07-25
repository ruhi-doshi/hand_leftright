import cv2 
import mediapipe as mp
from google.protobuf.json_format import MessageToDict

mp_hands = mp.solutions.hands 
hands = mp_hands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=2
) 

mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0) 

# Initialize variables for tracking movement
previous_y = None
movement_threshold = 5  # Adjust as necessary

while True: 
    success, img = cap.read()
    if not success:
        break
  
    img = cv2.flip(img, 1)
  
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  
    results = hands.process(imgRGB)
  
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            
            h, w, c = img.shape
            wrist_x, wrist_y = int(wrist.x * w), int(wrist.y * h)
            
            # Movement detection
            if previous_y is not None:
                if wrist_y < previous_y - movement_threshold:
                    cv2.putText(img, 'Up', (wrist_x, wrist_y - 20), 
                                cv2.FONT_HERSHEY_COMPLEX, 
                                0.9, (0, 255, 0), 2)
                elif wrist_y > previous_y + movement_threshold:
                    cv2.putText(img, 'Down', (wrist_x, wrist_y - 20), 
                                cv2.FONT_HERSHEY_COMPLEX, 
                                0.9, (0, 0, 255), 2)
            if len(results.multi_handedness) == 2:
                cv2.putText(img, 'Both', (20, 20),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.9, (0, 255, 0), 2)
            else:
                for i in results.multi_handedness:
                    label = MessageToDict(i)['classification'][0]['label']
  
                    if label == 'Left':
                        cv2.putText(img, label, (20, 20),
                                    cv2.FONT_HERSHEY_COMPLEX, 
                                    0.9, (0, 255, 0), 2)
                    if label == 'Right':
                        cv2.putText(img, label, (20, 20),
                                    cv2.FONT_HERSHEY_COMPLEX, 
                                    0.9, (0, 255, 0), 2)  
            previous_y = wrist_y
  
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
