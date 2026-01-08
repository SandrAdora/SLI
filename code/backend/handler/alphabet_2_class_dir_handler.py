###################################################################################
# This File is a handler file, it provides a range of functions to help the system#
# These methods are helper methods to help speed up redundant tasks               #
#                                                                                 #
# Author: Sandra Edigin                                                           #
# Creation Date: 03.01.2026                                                       #
# Version: 1.0                                                                    #
###################################################################################


# Create an alphabet to class dictionary 
def create_alphabet_to_class_dic(number_of_classes: int=26):
    """This Function creates a dictionary of classes equivalent to their alphabet
    The default is 26 classes.
    Args:
        number_of_classes (int): The number of classes as digits
    Returns:
        dic (dict): A dictionary of classes mapped with their corresponding  alphabets""" 
    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alphabet_to_class={}
    # Map Class to alphabets
    for i in range(number_of_classes):
        alphabet_to_class[alphabets[i]]=i
    return alphabet_to_class
