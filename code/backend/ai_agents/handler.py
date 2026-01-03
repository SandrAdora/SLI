###################################################################################
# This File is a handler file, it provides a range of functions to help the system#
# These methods are helper methods to help speed up redundant tasks               #
#                                                                                 #
# Author: Sandra Edigin                                                           #
# Creation Date: 03.01.2026                                                       #
# Version: 1.0                                                                    #
###################################################################################
import cv2 
import os
import numpy as np
from logging import raiseExceptions

# Create an alphabet to class dictionary 
def create_alphabet_to_class_dic(number_of_classes: int):
    """This Function creates a dictionary of classes equivalent to their alphabet
    Args:
        number_of_classes (int): The number of classes as digits
    Returns:
        dic (dict): A dictionary of classes mapped with their corresponding  alphabets"""
    
    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alphabet_to_class ={}
    
    for i in range(len(number_of_classes)):
        alphabet_to_class[alphabets[i]]=i
    return alphabet_to_class

# Create different varieties of an image
def agumented_images(img):
    """This function clones imgs"""
    augmented=[]
    
    # flip horizontaly 
    augmented.append(cv2.flip(img, 1))
    # rotate to 15 degrees 
    m=cv2.getRotationMatrix2D((img.shape[1]//[2], img.shape[0]//2), 15,1)
    augmented.append(cv2.warpAffine(img, m, (img.shape[1], img.shape[0])))
    
    # add gaussian noise to simulate the different camera versions 
    noise=np.random.normal(0, 15, img.shape).astype(np.uint8)
    augmented.append(cv2.add(img,noise))
    # add and decrease brightness to stimulate different lighting options
    augmented.append(cv2.convertScaleAbs(img, alpha=1.2, beta=20))
    augmented.append(cv2.convertScaleAbs(img, alpha=0.8, beta=-20))
    return augmented


# Generate an image   
def img_generator(alphabet: str, numbers_of_dataset:int, img_path:str,img_alph: str) -> str:
    """This function generates a specified amount of img dataset for a defined alphabet. The format of the img will be .jpg
    Args:
        alphabet (str): The Alphabet 
        numbers_of_dataset (int): The amount of dataset of the alphabet that should be cloned
        img_path (str): Path to the image  and the destination
    Returns:
        str (str): A notification that files were generated"""
    
    # Check if path exist and end script if it doesnt 
    fullpath=os.path.join(img_path, img_alph)
    if not os.path.exists(fullpath):
        print("Error: Path does not exit")
        exit()
    # clone img
    for i in range(numbers_of_dataset):
        for aug in agumented_images(img_alph):
            filename=os.path.join(img_path, f"img_{i}_{alphabet}.jpg")
            cv2.imwrite(filename, aug)    
    return f" {numbers_of_dataset} Images for Sign Language {alphabet} have been created."