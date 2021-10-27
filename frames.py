from __future__ import unicode_literals
import numpy as np
import cv2

vidcap = cv2.VideoCapture('olcar.mp4')
total_frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
frames_step = total_frames//30
for i in range(30):
    #here, we set the parameter 1 which is the frame number to the frame (i*frames_step)
    vidcap.set(1,i*frames_step)
    success,image = vidcap.read()  
    #save your image
    path='C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/video img/'+str(i)+'.jpeg'
    cv2.imwrite(path,image)
vidcap.release()