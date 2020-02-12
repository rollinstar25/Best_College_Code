# -*- coding: utf-8 -*-
import cv2
import numpy as np
import random
import tarfile
import os

try:
    import wget
except:
    import pip
    pip.main(['install', 'wget'])
    import wget
"""
Project 2 :
    Gracie Street/ mstreet@rollins.edu
    Collaboration Statement:
        I worked on this project alone using only course materials provided,
        as well as additional outside sources
        Outside Sources:
            http://www.drdobbs.com/understanding-photomosaics/184404848
            http://vision.stanford.edu/aditya86/ImageNetDogs/
            https://docs.python.org/2/library/random.html
Created on Fri Oct 27 12:12:47 2017

@author: Grace Street
"""

"""
Psuedo:
    1.Take a scanned photo (source image) to process.
    2.Make a grid over this photo.
    3.Look at every cell on the grid.
    4.Calculate the average color of each cell.
    5.Find the nearest image in the library with the same average color of the cell and substitute it in that cell.
    6.Repeat the process for each cell in the grid.
    
    Think of the cell as a kernel, and you are pushing along moving on to the next cell
    Adjust size will have to be a pyramid blur
"""

#url = 'http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar'
#dataset = wget.download(url)
#image_dataset = tarfile.open('images.tar', mode='r')

directory_name = 'C:/Users/Grace/Documents/Classes/Junior/Python/Projects/Project2/light_yagami_face'
#print(os.listdir(directory))

img_path_list = []
dir_path_list = []
image_list = []

    

def combined_path(directory_path, img_path):
    """
    This function creates an image from paths
    
    Args:
        directory_path: the path leading to directory
        img_path: the path leading to the image in directory
    
    Returns:
        image: the image located at the math
    """
    image_location = directory_path + '/' + img_path
    #os.path.join(image_location)
    return image_location

def get_image_paths(directory):
    """
    This function adds directory paths to a list and file paths to another list
    
    Args:
        directory: the directory being looped through
        
    """
    #Creates a list from a directory
    files = os.listdir(directory)
    #Im going through the list and checking if it is a directory,
    #if it is a directory I add the path to the list, then recurse to the top
    #so that I can add all paths to images from that file into a separate list
    for f in files:
        dir = directory +'/'+ f
        if os.path.isdir(dir):
            dir_path_list.append(dir)
            get_image_paths(dir)
        else:
           img_path_list.append(f)

def clear_list(list):
    """
    This function empties out a list of all its values.
    
    Args:
        list: list being cleared
    """
    
    for e in list:
        list.remove(e)

def crop(image):
   """
   This function crops an image into even proportions, or in a square.
   I received help and ideas from Rene Borr.

   Args: 
       image: the image being cropped
       
   Returns:
       cropped: cropped image
   """
   cropped = image.copy()
   rows, cols, channels = cropped.shape
    
   if(rows >= cols):
       size = cols
   else:
       size = rows
   cropped = image[0:size][0:size]
   return cropped
    
def change_image_size(image, size):
    """
    This function changes the size of an image
    I received help and ideas from Rene Borr
    
    Args:
        image: the image being sized
        
        size: the length/ width that the image is being sized to
    
    Returns:
        changed: the new sized image
    """
    changed = cv2.resize(image, (size,size))
    return changed

def adjust_size(image, size):
    """
    This function Gaussian blurs and adjusts the size of an image to be placed
    in the mosaic.
    
    Notes:
        I added a checking statement to ensure the user does not input a
        size that is too large to recognize what something is. I set the 
        minimum number of cells to 10, for that same reason. 
    
    Args:
        image: the image being adjusted
        
        size: the length/width that the image is to be sized to.
        
    Returns:
        reduced_image: the final reduced image

    """
    resize = image.copy
    rows, cols, chan = resize.shape
    if (size * size) > (rows * cols / 10):
        print("Please choose a smaller size.")
    resize = image.astype(np.float32)
    gauss_blur = cv2.GaussianBlur(resize, (5,5), 1.7  )
    adjusted_image = gauss_blur[::2,::2]
    reduced_image = change_image_size(resize, size)
    return reduced_image

def average_color_value(image):
    """
    This function calculates the average color value of an image, cell, or kernel 
    of pixels.
    
    Args:
        image: image which is used
        
    Returns:
        b_avg: the average blue color value of image
        g_avg: the average green color value of image
        r_avg: the average red color value of image
    """
    avg_img = image.copy()
    row, col, chan = avg_img.shape
    r_sum = 0
    g_sum = 0
    b_sum = 0
    for r in range(0, row, 1):
        for c in range(0, col, 1):
           r_sum = r_sum + avg_img[r][c][2]
           g_sum = g_sum + avg_img[r][c][1]
           b_sum = b_sum + avg_img[r][c][0]
    b_avg = b_sum / (row * col)
    g_avg = g_sum / (row * col)
    r_avg = r_sum / (row * col)
    
    return b_avg, g_avg, r_avg
    
def find_match(dataset, main_image):
    """
    This function searchs a library/ dataset of images for an image with 
    an average color value equivalent to that of a specified cell in another
    image.
    
    Notes:
        This is assuming that the dataset is actually expressed in an array
        that can be iterated through.
    
    Args:
        main_image: the image that is being matched
        
        dataset: the library/ dataset of images being pulled from
        
    Returns:
        matching_image: if a matching image is found, then it will be returned
        
    """
    image = main_image.copy()
    matching_image = 0
    b_value, g_value, r_value = average_color_value(image)
    for f in range(0, len(dataset), 1):
        found_image = dataset[f]
        blue, green, red = average_color_value(found_image)
        if blue == b_value and green == g_value and red == r_value:
            matching_image = found_image
            break
    return matching_image

def mosaic(main_image, library, size):
    """
    This function creates a photomosaic when given a base image, a library
    of images and the desired size for each image.
    
    Notes:
        This function assumes that every image are perfect squares in that 
        they have the same length and width.
    
    Args:
        main_image : the base image that is going to be made into a mosaic
        
        library : the library or data set of images that will be used to make
                  the mosaic.
                  
        size: the size that every image placed in the mosaic will be.
        
    Returns:
        mosaic_image: the final image in mosaic form
    """
    mosaic_image = main_image.copy()
    num_rows, num_cols, channels = mosaic_image.shape
    cell = np.zeros((size,size, 3))#create kernel / "grid"
    for row in range(0, num_rows - 1, size): # running through image pixels
        for col in range(0, num_cols - 1, size):
           for x in range(0, size, 1): #running through kernel pixels#adjust
              for y in range(0, size, 1):
                  cell[x][y] = mosaic_image[row + x][col + y] #copying image values into kernel
           new_image = find_match(library, cell)#finding image with matching color average
           smaller_img = adjust_size(new_image, size)#resizing to fit into kernel
           rows, cols, channels = smaller_img.shape
           for r in range(0, rows, 1): #have to iterate through kernel again...
               for c in range(0, cols, 1):
                   mosaic_image[row + r][col + c] = smaller_img[r][c] #setting new image values#adjust 
    
    return mosaic_image
    
    
"""
Main part of function
I plan to generate a random number as an index to the data set of the images
Basically, creating a mosaic from a random picture every time
"""
get_image_paths(directory_name)#fills image and directory arrays
#clear_list(img_path_list)#clears image array
#rand_file_index = random.randrange(0, len(dir_path_list), len(dir_path_list))
#get_image_paths(dir_path_list[rand_file_index])#fills the list with paths to images
#rand_img_index = random.randrange(0, len(img_path_list), len(img_path_list))

main_image = img_path_list[13]

#main_directory = dir_path_list[rand_file_index]
in_image_name = combined_path(directory_name, main_image)

#Making a for loop to fill the image list with cropped images
i = 0
for i in range(0, len(img_path_list), 1):
    new_image_name = combined_path(directory_name, img_path_list[i])                                                                #this element keeps coming out as a none type
    new_image = cv2.imread(new_image_name)
    cropped = crop(new_image)
    image_list.append(cropped)

main_image = image_list[13]
#50 x 50 pixel cells
out_image50 = mosaic(main_image, image_list, 50)
#75 x 75 pixel cells
#out_image75 = mosaic(in_image, main_image, 75)
#100 x 100 pixel cells
#out_image100 = mosaic(in_image, main_image, 100)

cv2.imshow("Original", main_image)
cv2.imshow("Mosaic x 50", out_image50)
"""
cv2.imshow("Mosaic x 75", out_image75)
cv2.imshow("Mosaic x 100", out_image100)
"""

cv2.waitKey(0)
cv2.destroyAllWindows()

""" Reading from Tar file notes
https://docs.python.org/2/library/tarfile.html
http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

I could create a textfile with all the names of the images and set that equal
to an array, that way I can freely access the names individually
"""




