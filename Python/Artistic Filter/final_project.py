# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 09:55:53 2017

@author: Grace Street
mstreet@rollins.edu

Final Project:  InstaArtist

The objective is to create the effect that objects in the camera's view 
are made to look like cartoons.

Honor Code: On my honor, I have not given, nor received, nor witnessed any 
unauthorized assisatnce on this work.

Collaboration Statement: I worked on this project alone, using cited online
materials and class materials provided.

I definitely need to use feature detection, but need to find a way to affect
sensitivity and thickness of lines.
You have the option of black board effect or sketch

I would like to have multiple art effect:
    sketch
    cartoon
    pop art
    watercolor

If there's time, see what I can do with GUIS
-> Ideally I'd like to give options to display images after transformations, 
before writing them.
-> Has the option of opening web cam for video

Sources:
    cartoon -> https://github.com/mbeyeler/opencv-python-blueprints/blob/master/chapter1/filters.py
    https://www.learnopencv.com/non-photorealistic-rendering-using-opencv-python-c/
    https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html

"""

import cv2
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from scipy.interpolate import UnivariateSpline


def apply_cartoon_filter(image):
    """
    This function takes an image and cartoonizes using a bilateral filter and 
    edge detection. 
    
    Args:
        image -> image being altered
        
    Returns:
        img_cartoon -> final cartoonized picture
    """
    img_rgb = image.copy()
    img_rgb = cv2.edgePreservingFilter(img_rgb, flags=1, sigma_s=60, sigma_r=0.4)
    
    numDownSamples = 2       # number of downscaling steps
    numBilateralFilters = 7  # number of bilateral filtering steps

    # -- STEP 1 --
    # downsample image using Gaussian pyramid
    img_color = img_rgb
    for x in range(numDownSamples):
        img_color = cv2.pyrDown(img_color)

    # repeatedly apply small bilateral filter instead of applying
    # one large filter
    for x in range(numBilateralFilters):
        img_color = cv2.bilateralFilter(img_color, 9, 9, 7)

    # upsample image to original size
    for x in range(numDownSamples):
        img_color = cv2.pyrUp(img_color)

    # -- STEPS 2 and 3 --
    # convert to grayscale and apply median blur
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)

    # -- STEP 4 --
    # detect and enhance edges
    img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY, 9, 2)

    # -- STEP 5 --
    # convert back to color so that it can be bit-ANDed with color image
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    
    #Need to check the size
    x, y, channel = img_color.shape
    resized_edge = cv2.resize(img_edge, (y, x))
    #print(img_edge.shape, img_color.shape, resized_edge.shape)
    
    img_cartoon = cv2.bitwise_and(img_color, resized_edge)
    return img_cartoon
    
def apply_pencil_sketch_filter(image):
    """
    This function takes an image and creates a pencil sketch version.
    
    Args:
        image -> the image
    
    Returns:
        sketch -> the final sketched image
        color -> the colored version of the sketch
    """
    sketched = image.copy()
    sketched_blur = cv2.GaussianBlur(sketched, (5,5), 1.7)
    #sketched_blur = cv2.medianBlur(sketched, 3)
    sketch, color = cv2.pencilSketch(sketched_blur,sigma_s=60, sigma_r=0.07, shade_factor=0.05)
    
    return sketch, color
    
def apply_black_board_filter(image):
    """
    This function basically inverts the pencil sketch function, creating a 
    black board effect
    
    Args:
        image -> the image
    
    Return:
        black_board -> final filtered image
    """
    blackboard = image.copy()
    sketched, colorsketch = apply_pencil_sketch_filter(blackboard)
    black_board = cv2.bitwise_not(sketched) #"not" the sketch creates the inverse
    
    return black_board
    
def apply_water_color_filter(image):
    """
    This function takes an image and produces a water color version of it.
    
    Args:
        image -> the image
        
    Return:
        water_color -> the final watercolor image
    """
    waterclr = image.copy()
    watercolor = cv2.edgePreservingFilter(waterclr, flags=1, sigma_s=60, sigma_r=0.4)
    watercolor = cv2.blur(watercolor, (5,5), 1.7)
    
    return watercolor
    
    
    
   
def video_application(cartoon = False, sketch = False, black_board = False, 
                      recording = False):
    """
    This function serves as the kiosk for choosing a photo effect to apply to 
    live video feed.
    
    Args: 
        cartoon -> True if a cartoon look is desired
        sketch -> True if a sketched look is desired
        black_board -> True if a blackboard effect is desired
    """
    capture = cv2.VideoCapture(0)
    
    #if we want a recording, set up the video writer
    if recording == True:
        ret, frame = capture.read()
        
        frame_size = (frame.shape[1], frame.shape[0])
        
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        out = cv2.VideoWriter()
        if sketch == True or black_board == True or sketch == True:
            out.open('output.wmv',fourcc, 20, frame_size, False)
        else:
            out.open('out_put.wmv', fourcc, 20, frame_size, True)
    
    while True:
       ret, frame = capture.read()
       
       if cartoon == True:
           frame = apply_cartoon_filter(frame)
           if recording == True:
               out.write(frame)
           cv2.imshow('Cartoon', frame)
           
       elif sketch == True:
           frame, color_filter = apply_pencil_sketch_filter(frame)
           if recording == True:
               out.write(frame)
               print("Printing frame")
           cv2.imshow('Sketch', frame)
       
       elif black_board == True:
           frame = apply_black_board_filter(frame)
           if recording == True:
               out.write(frame)
           cv2.imshow('BlackBoard', frame)
           
 
       else:
           if recording == True:
               out.write(frame)
           cv2.imshow('No Filter', frame)
           
       
       #Press c to capture an image and if there's a recording it will 
       #write both image and video and exit
       if cv2.waitKey(1) & 0xFF == ord('c'):
           out_put = cv2.imwrite('capture.jpg', frame)
           break
    
    capture.release()
    #release the video recording
    if recording == True:
        out.release()
        out = None
    cv2.destroyAllWindows()
       
        
    
    
       
    
    
    
    
"""
MAIN
"""
"""
IMAGES
"""
"""
in_image = cv2.imread("silly_string.png")
out_image_car = apply_cartoon_filter(in_image)
out_image_sketch, out_put_color_sketch = apply_pencil_sketch_filter(in_image)
out_image_blkbrd = apply_black_board_filter(in_image)

cv2.imwrite('cartoon_string.png', out_image_car)
cv2.imwrite('black_string.png', out_image_blkbrd)
cv2.imwrite('sketch_string.png', out_image_sketch)
#out_image_water_color = apply_water_color_filter(in_image)
"""
"""
cv2.imshow('Original', in_image)
cv2.imshow('Cartoon', out_image_car)

cv2.imshow('Sketch', out_image_sketch)
cv2.imshow('BlackBoard', out_image_blkbrd)
#cv2.imshow('WaterColor', out_image_water_color)#need to keep tying to find 
                                                #better way to make effect
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
"""Video(Change the following to True or false depending on your desired out put)"""
#video_application(cartoon = False, sketch = False, black_board = True, 
#               recording = True) 
       
       
       
       
       
       
       
