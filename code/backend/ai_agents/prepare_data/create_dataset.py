###################################################
# This program creates the dataset for Classifier #
# only applicable for real hands                  #s
###################################################

import os
import cv2
import pickle
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Path to your augmented images
DATA = './data/'

# Path to the new MediaPipe model
MODEL_PATH = 'models/hand_landmarker.task'

# Load the new MediaPipe Hand Landmarker
base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.3,
    min_hand_presence_confidence=0.3,
    min_tracking_confidence=0.3
)
landmarker = vision.HandLandmarker.create_from_options(options)

# Storage for dataset
data = []
labels = []

# Process each class folder
for dir_ in os.listdir(DATA):
    class_path = os.path.join(DATA, dir_)

    for img_pth in os.listdir(class_path):
        img_path = os.path.join(class_path, img_pth)

        # Load image
        img = cv2.imread(img_path)
        if img is None:
            print(f"Could not load image: {img_path}")
            continue

        # Convert to MediaPipe Image
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img)

        # Run hand landmark detection
        result = landmarker.detect(mp_image)

        if not result.hand_landmarks:
            continue

        # Extract x,y coordinates
        data_xy = []
        hand = result.hand_landmarks[0]

        for lm in hand:
            data_xy.append(lm.x)
            data_xy.append(lm.y)

        data.append(data_xy)
        labels.append(dir_)

# Save dataset
with open('data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)

print("Dataset created successfully!")
print(labels)
