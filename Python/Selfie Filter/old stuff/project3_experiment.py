# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 20:40:48 2017
Project 3 SnapChat Filters Upgraded

@author: Grace Street and Sierra Sarver
SSARVER@rollins.edu
MSTREET@rollins.edu

On our honor we have not given nor received nor witnessed any unauthorized 
assistance on this work.

Collaboration Statement: We worked alone on this project using only authorized 
class materials and online resources.
Online Resources:
    video capture-> https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/
                     py_video_display/py_video_display.html#display-video
                 -> https://realpython.com/blog/python/
                    `aface-detection-in-python-using-a-webcam/
                ->  https://www.youtube.com/watch?v=88HdqNDQsEk&t=586s
    
"""
import cv2
import numpy as np
from PIL import Image


"""
We want to apply various snapchat selfie filters using live video feeds.
"""

#Im not sure how we want to do these methods yet

#Might want to use this: https://stackoverflow.com/questions/30110018/
#opencv-with-python-placing-an-image-of-a-hat-over-the-head-of-a-webcam-feed
#as a reference to putting images over videos
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
    while True :
    # Capture frame-by-frame
       ret, frame = video.read()
    
    # Our operations on the frame come here
    #The reason we convert to gray first is because it's better for the detection
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
       faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #Draw a rectangle around the faces(Green)
       for (x, y, w, h) in faces:
          #cv2.rectangle(frame, (x, y), (x+w, y+h),(0, 255, 0), 0)
          dog_image = cv2.resize(dog_face, (h, w))
          roi_gray = gray[y:y+h, x:x+h]
          roi_color = frame[y:y+h, x:x+h]
          
          dog_img = cv2.add(dog_image, roi_color)
          roi_color[0:h, 0:w] = dog_img
       """
          eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 2)
        #Draws the rectangle around the eyes(Blue)
          for (ex, ey, ew, eh) in eyes:
             cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
        #For the following rectangles, I had to guesstimate where those features are on the average person
        #Be careful messing with these, parentheses and stuff like that...
        #Draws the rectangle for the nose at the center of the rectangle for face (Teal)
          cv2.rectangle(frame, (int((x+(w/2))-(ew/2.5)), int((y+(h/2))-(eh/2.5))), (int((x+(w/2))+(ew/2.5)), int((y+(h/2))+(eh/2.5))), (255, 255, 0), 2)
        #Draws the rectangle for the mouth at about 2/3 of the way down the face rectangle (Purple)
          cv2.rectangle(frame, (int(x+(w/3)), int(y+((2/3)*h))), (int((x+((2/3)*w))), int((y+((2/3)*h))+eh)),(255, 0, 255), 2)
    """
          # Display the resulting frame
       cv2.imshow('DogFace', frame)
    #Press the 'q' key to close the video feed
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
    eye_pic = read_transparent_png('heartEyes.png')
    
    while True :
    # Capture frame-by-frame
       ret, frame = video.read()
    
    # Our operations on the frame come here
    #The reason we convert to gray first is because it's better for the detection
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
       faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #Draw a rectangle around the faces(Green)
       for (x, y, w, h) in faces:
          #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
          roi_gray = gray[y:y+h, x:x+h]
          roi_color = frame[y:y+h, x:x+h]
          eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 2)
        #Draws the rectangle around the eyes(Blue)
          for (ex, ey, ew, eh) in eyes:
             #cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
             roi_eye_color= roi_color[ey:ey+eh, ex:ex+eh]
             eye_image = cv2.resize(eye_pic, (eh, ew))
             
             heart_eyes = cv2.add(eye_image, roi_eye_color)
             roi_eye_color[0:eh, 0:ew] = heart_eyes
       # Display the resulting frame
       cv2.imshow('HeartEyes', frame)
    #Press the 'q' key to close the video feed
       if cv2.waitKey(1) & 0xFF == ord('q'):
          break
    
def hat_filter(video):
   """
   This method applies the dog face filter onto the video.
   It draws rectangles in the corresponding places of interest for this filter.
   In this case, it is the face, eyes, nose and mouth.
    
   The objective is to place images of the dogs facial features on top of 
   the corresponding facial features of the person.
    
   Args:
   video -> video we are applying to filter to
   """
   hat = cv2.imread('hat.png')
   while True :
   # Capture frame-by-frame
      ret, frame = capture.read()
    
   # Our operations on the frame come here
   #The reason we convert to gray first is because it's better for the detection
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
      faces = face_cascade.detectMultiScale(gray, 1.3, 5)
   #Draw a rectangle around the faces(Green)
      for (x, y, w, h) in faces:
         #cv2.rectangle(frame, (x, y), (x+w, y+h),(0, 255, 0), 0)
         hat_image = cv2.resize(hat, (w, w))
         #roi_color = frame[y:y+h, x:x+w]
          
         hat_img = cv2.add(hat_image, frame)
         frame[y-w:y-10, x:x+w] = hat_img
      
      
      
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
    while True :
    # Capture frame-by-frame
       ret, frame = video.read()
       
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       face_1 = face_cascade.detectMultiScale(gray, 1.3, 5)
    #Draw a rectangle around the faces(Green)
       for (x, y, w, h) in face_1:
          cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
       """
       x, y, channel = frame.shape
       #I need to make a copy that is the same size as my 
       #frame.
       other_layer = frame.copy()
       
       #Rectangle 1
       x1 = int((x/2) - (x/3))
       y1 = int(y / 5)
       x2 = int((x/2)- 10)
       y2 = int(y - (y/3))
       
       #Rectangle 2
       x3 = int((x/2) + 10)
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
"""
       
       
    # Display the resulting frame
       cv2.imshow('FaceSwap', frame)
    #Press the 'q' key to close the video feed
       if cv2.waitKey(1) & 0xFF == ord('q'):
          break
    
    
    
    
    
    
"""
This captures the video
You can ignore, heart eyes and buck teeth and use the filters you want, but 
they do have the tracking for nose and mouth if you like.
"""
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
capture = cv2.VideoCapture(0)
#face_swap(capture)
#dog_face_filter(capture)
hat_filter(capture)
#heart_eyes_filter(capture)

        # When everything done, release the capture
capture.release()
cv2.destroyAllWindows()
