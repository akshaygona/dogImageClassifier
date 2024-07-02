#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Akshay Gona
# DATE CREATED: 06/24/2024                          
# REVISED DATE: 07/01/2024
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    
    results_dic = {}

    for filename in listdir(image_dir):
        if not filename.startswith('.'):
            file_parts = filename.lower().split('_')
            label = ' '.join([part for part in file_parts if part.isalpha()])
            if filename not in results_dic:
                results_dic[filename] = [label]
            else:
                results_dic[filename].append(label)

    return results_dic
