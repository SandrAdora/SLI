###################################################
# This program only shows the landmarks on the img#
###################################################
import os
import mediapipe as mp 
import cv2
import matplotlib.pyplot as plt


# setting up handmarks
mp_hands = mp.solutions.hands
mp_drawings = mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles

hands=mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3) 

DATA ='./data'

for dir_ in os.listdir(DATA):
    for img_pth in os.listdir(os.path.join(DATA, dir_)):
        img = cv2.imread(os.path.join(DATA, dir_, img_pth))
        img_rgb=cv2.cvtColor(img , cv2.COLOR_BAYER_BG2BGR)
        
        # detect all the landmarks into the image
        result=hands.process(img_rgb)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawings.draw_landmarks(
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )
        
        plt.figure()
        plt.imshow(img_rgb)

plt.show()