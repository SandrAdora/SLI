###################################################
# This program creates the dataset for Classifier #
#                                                 #
###################################################

import os
import mediapipe as mp 
import cv2
import matplotlib.pyplot as plt
import pickle

# setting up handmarks
mp_hands = mp.solutions.hands
mp_drawings = mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles


hands=mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3) 

# Get the Images
DATA ='./data'

# Store the datasets
data=[]
labels=[]

# detect the landmarks and extract the x and y coordinates of the landmarks
for dir_ in os.listdir(DATA):
    for img_pth in os.listdir(os.path.join(DATA, dir_)):
        data_xy=[]
        img = cv2.imread(os.path.join(DATA, dir_, img_pth))
        img_rgb=cv2.cvtColor(img , cv2.COLOR_BAYER_BG2BGR)
        
        # detect all the landmarks into the image
        result=hands.process(img_rgb)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Get the x and y coordinates from the img which will be our
                # X-dataset and Y dataset 
                for i in range(len(hand_landmarks.landmark)):
                    X =  hand_landmarks.landmark[i].x 
                    y = hand_landmarks.landmark[i].y
                    data_xy.append(X)
                    data_xy.append(y)
            data.append(data_xy)
            labels.append(dir_)
        

# Generate the file data.pickle and store dataset from lists data and labels in it      
f=open('data.pickle', 'wb')
pickle.dump({'data': data, 'labels':labels}, f)
f.close()