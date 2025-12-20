import cv2
import mediapipe as mp

# capture video from camera
cap = cv2.VideoCapture(0)

hands = mp.solutions.hands 
hand_detector = hands.Hands(static_image_mode=False,
                            max_num_hands=2,
                            min_detection_confidence=0.5,
                            min_tracking_confidence=0.5)
hand_draw = mp.solutions.drawing_utils