
import os
import cv2
import csv 

DATA="./data/augmented/"
CSV_OUT="./data/"

with open(CSV_OUT, "w", newline="") as file:
    writer=csv.writer(file)
    # setup labels 
    for label in os.listdir(DATA):
        class_dir=os.path.join(class_dir, label)
        # get the images 
        for img_name in os.listdir(class_dir):
            img_path=os.path.join(class_dir, img_name)
            
            #  load img
            img=cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            
            # resize img to 28x28 
            img=cv2.resize(img,(28,28) )
            #  flatten 
            pixels=img.flatten().tolist()
            
            # write label to pixes for each row 
            writer.writerow([label] + pixels)