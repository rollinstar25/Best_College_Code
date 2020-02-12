# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:56:41 2017

@author: Grace Street
mstreet@rollins.edu

Honor Code: On my honor, I have not given, nor received, nor witnessed any 
unauthorized assisatnce on this work.

Collaboration Statement: I worked on this project alone, using cited online
materials and class materials provided.

Final Project: InstaArtist - GUI

This section contains code for making and maintaining a GUI for the InstaArtist
program

Sources:
    https://www.tutorialspoint.com/python/python_gui_programming.htm
    https://www.learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/

"""
import cv2
import numpy as np
import scipy as sp
import tkinter as tk
from tkinter import Menu
from tkinter import *

from PIL import ImageTk, Image
import final_project as fp
 


def image_selection(variable):
    """
    This function chooses the image to be altered and displays it
    
    Args:
        variable -> integer variable representing the picture
    """
    global image_name 
    
    if variable == 1:
        image_name = "street_side.png"
    elif variable == 2:
        image_name = "bottle.png"
    elif variable == 3:
        image_name = "silly_string.png"
        
    return image_name
        
        
        
def retrieve_effect(effect_num, name):
    """
    This function applies the desired filter to the image
    
    Args:
        effect_num -> number representing the desired effect
        name -> the name of the image
    """
    
    global in_image
    global filtered
    global effect 
    
    
    #image_name = name
    effect = effect_num
    
    in_image = cv2.imread(name)
    filtered = in_image.copy()
    if effect_num == 1:
       filtered = fp.apply_cartoon_filter(filtered)
    elif effect_num == 2:
        filtered, clr= fp.apply_pencil_sketch_filter(filtered)
    elif effect_num == 3:
        filtered = fp.apply_black_board_filter(filtered)
    else:
        filtered = in_image
        
    return filtered
        
def webcam(effect_num):
    """
    This function allows the user to open the webcam to apply effects to a picture
    
    Args:
        effect_num -> number representing effect desired
    """
    
    if effect_num == 1:
        fp.video_application(cartoon = True)
    elif effect_num == 2:
        fp.video_application(sketch = True)
    elif effect_num == 3:
        fp.video_application(black_board = True)
    else:
        fp.video_application()
        
def record_video(effect_num):
    """
    This function allows the user to record a video with the web cam with the 
    desired effect applied to it
    
    Args:
        effect_num -> number representing the desired effect
    """
    
    if effect_num == 1:
        fp.video_application(cartoon = True, recording = True)
    elif effect_num == 2:
        fp.video_application(sketch = True, recording = True)
    elif effect_num == 3:
        fp.video_application(black_board = True, recording = True)
    else:
        fp.video_application(recording = True)
        
def display_image(in_image_name, out_image_name):
    """
    This function displays the original image and its altered form
    
    Args:
        in_image_name -> the input image
        out_image_name -> the output image
    """
    cv2.imwrite('new_image.png', out_image_name)
    cv2.imshow('Original', in_image_name)
    cv2.imshow('New', out_image_name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def image_menu(root, current):
    """
    This function selects the image that is to be altered.
    
    Args:
        root -> the root frame
        current -> the frame you want the menu to be in
    """
    # menu button for images
    mb=  Menubutton ( current, text="Select your image", relief=RAISED )
    #mb.grid()
    mb.menu =  Menu ( mb, tearoff = 0 )
    mb["menu"] =  mb.menu

    mb.menu.add_radiobutton ( label="Bottle", 
                             command = lambda: image_selection(1)) # These should be setting the global variable image_name
    mb.menu.add_radiobutton ( label="Street Side",
                             command = lambda: image_selection(2))
    mb.menu.add_radiobutton ( label="Silly String",
                             command = lambda: image_selection(3))
    mb.pack()
    
def effect_menu(root, current, image):
    """
    This function selects the effect that the image will have 
    
    Args:
        root -> the root frame
        current-> the frame you want the menu to be in
        
    """
    #menu button for effects
    mbe = Menubutton(current, text="Select your effect", relief=RAISED)
    mbe.menu = Menu (mbe, tearoff = 0)
    mbe["menu"] = mbe.menu
    mbe.menu.add_radiobutton( label = "Cartoon",
                             command = lambda: retrieve_effect(1, image)) #these should take the global image name and apply the effect
    mbe.menu.add_radiobutton( label = "Pencil Sketch",
                             command = lambda: retrieve_effect(2, image))
    mbe.menu.add_radiobutton( label = "Blackboard",
                             command = lambda: retrieve_effect(3, image))
    mbe.menu.add_radiobutton( label = "No Effect",
                             command = lambda: retrieve_effect(0, image))
    
    mbe.pack()
    
    
    

"""MAIN"""
filtered = ""
in_image = ""
image_name = ""
effect = ""
#Window begins
top = tk.Tk()

#Inserts Logo picture
logo = Image.open("instaartist_logo.png") #opens image
logo = ImageTk.PhotoImage(logo) # makes it compatible with label
logo_pic = Label(top, image=logo) #places image in label widget
logo_pic.pack() #packs in

# Right Side
right_frame = Frame(top, bg = "white") #creates a frame on the right side
right_frame.pack(side = RIGHT)

image_menu(top, right_frame) #creates a menu for images on the right side
effect_menu(top, right_frame, image_name) #creates a menu for effects on the right side

submit = Button(right_frame, text="Preview and Save",
                command= lambda: display_image(in_image, filtered))# button displays image
submit.pack() #packs button 

#Left Side
left_frame = Frame(top, bg = "white") # creates a frame on the left side
left_frame.pack(side = LEFT) 

capture = Button(left_frame, text="WebCam Capture",
                 command= lambda: webcam(effect)) # button allows for web cam capture
capture.pack()

video = Button(left_frame, text="Capture Video",
              command= lambda: record_video(effect)) # button allows for video recording
video.pack() #packs button



top.mainloop() # end of the GUI loop




