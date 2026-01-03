########################################################################################
# This program is a script create sign-language img using the webcam                   #
#                                                                                      #
# Author: Sandra Edigin                                                                # 
# Creation Date: 02.01.2026                                                            #
# Version: 1.0                                                                         #
########################################################################################

import os
import cv2
import time
from handler import create_alphabet_to_class_dic
# setup location to store the images
IMG_STORAGE = "./data"
if not os.path.exists(IMG_STORAGE):
    os.makedirs(IMG_STORAGE)
    

# set number of classes == folders and how many dataset in each folder
number_of_classes=26
dataset_size=100

# Setup the classes and the alphabets
alphabet_to_class_dic=create_alphabet_to_class_dic(number_of_classes=number_of_classes)

# Setup the webcam 
cap = cv2.VideoCapture(0) # index 0 == webcam
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()
for key,value in alphabet_to_class_dic.items():
    
    class_path = os.path.join(IMG_STORAGE, str(value) )
    os.makedirs(class_path, exist_ok=True)
    print(f"\nPreparing to collect data for class '{key}'")
    #  wait for user to start the script 
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Faile to grab frame")
        
        #  wait for user to start the script 
        cv2.putText(frame, "Ready? Press ENTER:"(50, 200),cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0),3)
        cv2.imshow("frame", frame)
        # Wait for the Enter Key
        enter_key=cv2.waitKey(2) & 0xFF == 13
        if enter_key == 113:
            break
    # start collecting the img
    count=0
    while count < dataset_size:
        ret,frame=cap.read()
        if not ret:
            print("Error: Failed to grab frame")
            break
        # Put a class Text on the screen for what class that img are collected for
        cv2.putText(frame, f"Class: {key}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # display the frame
        cv2.imshow("frame", frame)
        
        # save the frame 
        cv2.imwrite(os.path.join(class_path, f"img_{count}_{key}.jpg"), frame)
        count+=1
        print(f"Images taken: {count}")
        
        # Exit early if user presses q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # wait 3 sec before collecting img for the next class 
        time.sleep(3)

# release camera
cap.release()
cv2.destroyAllWindows()
        


