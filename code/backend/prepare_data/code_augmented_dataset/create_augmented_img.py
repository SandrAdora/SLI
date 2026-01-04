################################################################################################
# This program create a variation of Images using the augmented method                         #
#                                                                                              #
# Author: Sandra Edigin                                                                        #
# Creation Date: 03.12.2026                                                                    #
# Version: 1.0                                                                                 #
################################################################################################

import os
import sys
# add path to skript 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from handler import img_generator, create_alphabet_to_class_dic


# source directory
data_aug='./data/for_augmentation/'

# destination directory 
dest_data_aug= './data/augmented'
# check if path exists
if not os.path.exists(data_aug):
    print("Error: Path does not exist")
    exit()
elif not os.path.exists(dest_data_aug):
    os.makedirs(dest_data_aug) # create new dir if dest. dir. does not exist
    
    
# generate augmented images

# setup alphabets
alphabets=create_alphabet_to_class_dic(number_of_classes=26)
print(alphabets)

# Generate images
for key, _ in alphabets.items():
    
    filename=f"img_{key.lower()}.jpg"
    img_generator(alphabet=key.lower(), numbers_of_dataset=50,  img_source=data_aug, img_dest=dest_data_aug, img_alph=filename )