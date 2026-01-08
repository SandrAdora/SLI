
import cv2 
import os
import numpy as np

# Create different varieties of an image
def augumented_image(img):
    """This function creates different varities of images
    Arg:
        img (jpg): Image file format jpg
    Return:
        augmented (jpg): Augmented IMG """
    augmented=[]    
    # flip horizontaly 
    augmented.append(cv2.flip(img, 1))
    # rotate to 15 degrees 
    m=cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), 15,1)
    augmented.append(cv2.warpAffine(img, m, (img.shape[1], img.shape[0])))  
    # add gaussian noise to simulate the different camera versions 
    noise=np.random.normal(0, 15, img.shape).astype(np.uint8)
    augmented.append(cv2.add(img,noise))
    # add and decrease brightness to stimulate different lighting options
    augmented.append(cv2.convertScaleAbs(img, alpha=1.2, beta=20))
    augmented.append(cv2.convertScaleAbs(img, alpha=0.8, beta=-20))
    return augmented


# Generate an image   
def img_generator(alphabet: str, numbers_of_dataset:int,  img_source:str, img_dest:str, img_alph: str, number_of_classes:int = 26,) -> str:
    """This function generates a specified amount of img dataset for a defined alphabet. The format of the img will be .jpg
    Args:
        alphabet (str): The Alphabet 
        numbers_of_dataset (int): The amount of dataset of the alphabet that should be cloned
        img_path (str): Path to the image  and the destination
        img_alph (jpg): The Image as an alphabet in JPG format
    Returns:
        str (str): A notification that files were generated"""
    # Check if path exist and end script if it doesnt 
    fullpath=os.path.join(img_source, img_alph)
    if not os.path.exists(fullpath):
        print("Error: Path does not exit")
        exit()
    
    # load img
    img=cv2.imread(fullpath)
    if img is None:
        print(f"Error: Could not load image {fullpath}")
        return 

    # Create destination path for each class
    class_path=os.path.join(img_dest, alphabet)
    os.makedirs(class_path, exist_ok=True)
    
    count=0
    while count < numbers_of_dataset:
        
        for aug in augumented_image(img):
            filename=os.path.join(class_path, f"img_{count}_{alphabet}.jpg")
            cv2.imwrite(filename, aug)
            count+=1
            if count >= numbers_of_dataset:
                break
    return f" {numbers_of_dataset} Images for Sign Language {alphabet} have been created."