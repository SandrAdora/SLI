########################################################################################
# This program is a script with enables us create sign-language img using the webcam   #
#                                                                                      #
# Author: Sandra Edigin                                                                # 
# Creation Date: 02.01.2026                                                            #
# Version: 1.0                                                                         #
########################################################################################

import os
import cv2

# setup location to store the images
IMG_STORAGE = "./data"
if not os.path.exists(IMG_STORAGE):
    os.makedirs(IMG_STORAGE)
    

# set number of classes == folders and how many dataset in each folder
number_of_classes=3
dataset_size=100

# Setup the webcam 
cap = cv2.VideoCapture(0) # index 0 == webcam
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()
for i in range(number_of_classes):
    
    class_path = os.path.join(os.path.join(IMG_STORAGE, str(i) ))
    os.makedirs(class_path, exist_ok=True)
    print(f"Collecting Data for class {i}")
    
    # start collecting the img
    count=0
    while count < dataset_size:
        ret,frame=cap.read()
        if not ret:
            print("Error: Failed to grab frame")
            break
        cv2.imshow("frame", frame)
        
        # save the frame 
        cv2.imwrite(os.path.join(class_path, f"img_{count}.jpg"), frame)
        count+=1
        print(f"Images taken: {count}")
        
        # Exit early if user presses q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# release camera
cap.release()
cv2.destroyAllWindows()
        


