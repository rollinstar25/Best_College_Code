# -*- coding: utf-8 -*-
"""
Due on Tues. 11/28 @4PM
Project 3: SnapChat Filters - Upgraded from project 2

@author: Grace Street and Sierra Sarver
SSARVER@rollins.edu
MSTREET@rollins.edu

"On our honor we have not given nor received nor witnessed any unauthorized 
assistance on this work."

Collaboration Statement: We worked alone on this project using only authorized 
class materials and online resources.
Online Resources:
    video capture-> https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/
                     py_video_display/py_video_display.html#display-video
                 -> https://realpython.com/blog/python/
                    `aface-detection-in-python-using-a-webcam/
                 -> https://www.youtube.com/watch?v=88HdqNDQsEk&t=586s
                 -> https://github.com/kunalgupta777/OpenCV-Face-Filters/blob/master/filters.py
    
"""
import cv2
import numpy as np

"""
We want to apply various snapchat selfie filters using live video feeds.
"""

def read_transparent_png(img_name):
    """ This function takes in the name of an image that needs the background
        to be transparent rather than black. To do this, you have to read in the
        4th channel as an alpha channel and then set all the pixels to be 0%
        transparent rendered on a white background.
        
    Args:
        img_name (string): Name of the png image to read in with alpha channel
                           to set transparent background

    Returns:
        numpy.ndarray: The transparent final image
    """
    image_4channel = cv2.imread(img_name, cv2.IMREAD_UNCHANGED)
    alpha_channel = image_4channel[:,:,3]
    rgb_channels = image_4channel[:,:,:3]

    # White Background Image
    white_background_image = np.ones_like(rgb_channels, dtype=np.uint8) * 255

    # Alpha factor
    alpha_factor = alpha_channel[:,:,np.newaxis].astype(np.float32) / 255.0
    alpha_factor = np.concatenate((alpha_factor,alpha_factor,alpha_factor), axis=2)

    # Transparent Image Rendered on White Background
    base = rgb_channels.astype(np.float32) * alpha_factor
    white = white_background_image.astype(np.float32) * (1 - alpha_factor)
    final_image = base + white
    
    return final_image.astype(np.uint8)

def dog_face_filter(video):
    """
    This method applies the dog face filter onto the video.
    It draws rectangles in the corresponding places of interest for this filter.
    In this case, it is the face, eyes, nose and mouth.
    
    The objective is to place images of the dogs facial features on top of 
    the corresponding facial features of the person.
    
    Args:
        video -> video we are applying to filter to
    """
    dog_face = cv2.imread('dog_filter.png')
    
    while True:
        # Capture frame-by-frame
        ret, frame = capture.read()
    
        # Our operations on the frame come here
        # The reason we convert to gray first is because it's better for the detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            #cv2.rectangle(frame, (x, y), (x+w, y+h),(0, 255, 0), 0)
            dog_image = cv2.resize(dog_face, (w,h))
            roi_color = frame[y:y+h, x:x+h]
            dog_img = cv2.add(dog_image, roi_color)
            roi_color[0:h, 0:w] = dog_img

        # Display the resulting frame
        cv2.imshow('DogFace', frame)
        # Press the 'q' key to close the video feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break      
      
def heart_eyes_filter(video):
    """
    This method applies the heart eyes filter onto the video.
    It draws rectangles in the corresponding places of interest for this filter.
    In this case, it is the face and eyes.
    
    The objective is to place pictures of hearts on top of the eyes.
    
    Args:
        video -> video we are applying to filter to
    """
    eye_pic = cv2.imread('heartEyes.png')
    
    while True:
        # Capture frame-by-frame
        ret, frame = video.read()
    
        # Our operations on the frame come here
        #The reason we convert to gray first is because it's better for the detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            roi_gray = gray[y:y+h, x:x+h]
            roi_color = frame[y:y+h, x:x+h]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 2)

            for (ex, ey, ew, eh) in eyes:
                #cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
                roi_eye_color= roi_color[ey:ey+eh, ex:ex+eh]
                eye_image = cv2.resize(eye_pic, (eh, ew))
                heart_eyes = cv2.add(eye_image, roi_eye_color)
                roi_eye_color[0:eh, 0:ew] = heart_eyes
        
        # Display the resulting frame
        cv2.imshow('HeartEyes', frame)
        # Press the 'q' key to close the video feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
def mustache_filter(video):
    """
    This method applies a mustache onto the video.
    It draws rectangles in the corresponding place of interest for this filter.
    This filter approached the problem a little different in that it
    only uses the frontal face detection. It juxtaposes the frame with where an
    actual mustache should appear on the face. It uses the different objects
    that were returned from the haar cascade.
    
    The objective is to take an image of a mustache and place it on the mouth
    
    Args:
        video -> video we are applying to filter to
    """
    stache = cv2.imread('mustache_filter.png')
    
    while True:
        # Capture frame-by-frame
        ret, frame = capture.read()
    
        # Our operations on the frame come here
        # The reason we convert to gray first is because it's better for the detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        # Draw a rectangle around the faces(Green)
        for (x, y, w, h) in faces:
            width = w
            height = h

            # Reize mustache image to appear correctly
            stache_width = int(w * 0.4166666)+1
            stache_height = int(h * 0.142857)+1
            stache = cv2.resize(stache,(stache_width, stache_height))

            for i in range(int(0.62857142857*height), int(0.62857142857*height) + stache_height):
                for j in range(int(0.29166666666*width), int(0.29166666666*width) + stache_width):
                    for k in range(3):
                        if stache[i-int(0.62857142857*height)][j-int(0.29166666666*width)][k] < 235:
                            frame[y+i][x+j][k] = stache[i-int(0.62857142857*height)][j-int(0.29166666666*width)][k]
                
                
        # Display the resulting frame
        cv2.imshow('Mustache', frame)
        # Press the 'q' key to close the video feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def hat_filter(video):
    """
    This method applies a mustache onto the video.
    It draws rectangles in the corresponding place of interest for this filter.
    This filter approached the problem a little different in that it
    only uses the frontal face detection. It juxtaposes the frame with where an
    actual mustache should appear on the face. It uses the different objects
    that were returned from the haar cascade.
    
    The objective is to take an image of a mustache and place it on the mouth
    
    Args:
        video -> video we are applying to filter to
    """
    hat = cv2.imread('hat_filter.png')
    
    while True:
        # Capture frame-by-frame
        ret, frame = capture.read()
    
        # Our operations on the frame come here
        # The reason we convert to gray first is because it's better for the detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        # Draw a rectangle around the faces(Green)
        for (x, y, w, h) in faces:
            width = w
            height = h
            
            # Reisze hat image to appear correctly
            hat_width = width+1
            hat_height = int(0.35*height)+1
            hat = cv2.resize(hat,(hat_width,hat_height))

            for i in range(hat_height):
                for j in range(hat_width):
                    for k in range(3):
                        if hat[i][j][k] < 235:
                            frame[y+i-int(0.25*height)][x+j][k] = hat[i][j][k]
                
        # Display the resulting frame
        cv2.imshow('Hat', frame)
        # Press the 'q' key to close the video feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def hat_and_stache_filter(video):
    hat = cv2.imread('hat_filter.png')
    stache = cv2.imread('mustache_filter.png')
    
    while True:
        # Capture frame-by-frame
        ret, frame = capture.read()
    
        # Our operations on the frame come here
        # The reason we convert to gray first is because it's better for the detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        # Draw a rectangle around the faces(Green)
        for (x, y, w, h) in faces:
            width = w
            height = h
            
            # Resize hat and stache to appear correctly
            hat_width = width+1
            hat_height = int(0.35*height)+1
            mst_width = int(w * 0.4166666)+1
            mst_height = int(h * 0.142857)+1

            hat = cv2.resize(hat,(hat_width,hat_height))

            # Apply the hat
            for i in range(hat_height):
                for j in range(hat_width):
                    for k in range(3):
                        if hat[i][j][k] < 235:
                            frame[y+i-int(0.25*height)][x+j][k] = hat[i][j][k]
            # Apply the stache
            for i in range(int(0.62857142857*height), int(0.62857142857*height) + mst_height):
                for j in range(int(0.29166666666*width), int(0.29166666666*width) + mst_width):
                    for k in range(3):
                        if stache[i-int(0.62857142857*height)][j-int(0.29166666666*width)][k] < 235:
                            frame[y+i][x+j][k] = stache[i-int(0.62857142857*height)][j-int(0.29166666666*width)][k]
                
        # Display the resulting frame
        cv2.imshow('Hat and Stache', frame)
        # Press the 'q' key to close the video feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
      
def face_swap(video):
    """
    This method applies the face swap filter onto the video.
    It draws rectangles in the corresponding places of interest for this filter.
    In this case, it is only the face.
    
    The objective is to take video from one region and swap it with another. 
    people can use this to swap eachother's faces
    
    Args:
        video -> video we are applying to filter to
    """
    while True:
       # Capture frame-by-frame
       ret, frame = video.read()
       
       x, y, channel = frame.shape
       #I need to make a copy that is the same size as my 
       #frame.
       other_layer = frame.copy()
       
       #Rectangle 1
       x1 = int(x / 10)
       y1 = int(y / 5)
       x2 = int(x1 + (x/3))
       y2 = int(y - (y/3))
       
       #Rectangle 2
       x3 = int((x - x2))
       y3 = int(y / 5)
       x4 = int(x - (x/10))
       y4 = int(y - (y/3))
       
       #cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
       #cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 255, 0), 2)
       
       rectangle_1 = frame[y1:y2, x1:x2]
       rectangle_2 = frame[y3:y4, x3:x4]
       
       other_layer[y1:y2, x1:x2] = rectangle_2
       other_layer[y3:y4, x3:x4] = rectangle_1
       frame[y1:y2, x1:x2] = other_layer[y1:y2, x1:x2]
       frame[y3:y4, x3:x4] = other_layer[y3:y4, x3:x4]       
       
        # Display the resulting frame
       cv2.imshow('FaceSwap', frame)
       # Press the 'q' key to close the video feed
       if cv2.waitKey(1) & 0xFF == ord('q'):
          break

# Haar Cascade Pre Trained Classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Capture video
capture = cv2.VideoCapture(0)

# Filters
#face_swap(capture)
#dog_face_filter(capture)
#mustache_filter(capture)
#hat_filter(capture)
heart_eyes_filter(capture)
#hat_and_stache_filter(capture)   NOT WORKING

# When everything done, release the capture
capture.release()
cv2.destroyAllWindows()
