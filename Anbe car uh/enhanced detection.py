from __future__ import unicode_literals
import os
import glob
import easyocr
import datetime
import cv2
import numpy as np
from PIL import Image,ImageEnhance
import time


def contrast_enhancement(filenames):
    
    im = Image.open(filenames)
    enhancer = ImageEnhance.Contrast(im)
    factor = 1.5
    im_output = enhancer.enhance(factor)
    im_output.save('opp.png')
    ce_op=cv2.imread('opp.png')
    ce_op_dis=cv2.resize(ce_op,(550,600))
    cv2.imshow('contrast',ce_op_dis)
    time.sleep(5)
    return os.path.abspath('opp.png')

def sharpness_enhancement(con_img):
    im = Image.open(con_img)
    enhancer = ImageEnhance.Sharpness(im)
    factor = 1.5
    im_s_1 = enhancer.enhance(factor)
    im_s_1.save('oppp.png')
    sh_op=cv2.imread('oppp.png')
    sh_op_dis=cv2.resize(sh_op,(540,600))
    cv2.imshow('Sharpned',sh_op_dis)
    time.sleep(5)
    return os.path.abspath('oppp.png')

    
def brightness_enhancement():
    return 

def ocr(filenames):
    path = 'C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/13 i .png'
    #for filename in glob.glob(os.path.join(path, '*.jpg')):
    with open(path, 'r') as f:
    #img_pa='C:/Users/Asus/OneDrive/Desktop/juju/smrt goggles/codes/using web cam/download.png' 
        res_list=[]
        read=easyocr.Reader(['en'])
        result=read.readtext(path)
        for i in range(len(result)):    
            p=[]
            p.append(result[i][1])
            res_list.append(''.join(i for i in p))
    return res_list

def filters(image):
    img=cv2.imread(image)
    medi=cv2.medianBlur(img,3)
    medi_op=cv2.resize(medi,(540,600))
    cv2.imshow("median blur",medi_op)

def file_writer():
    return 

def frame_creator():
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

if __name__=="__main__":
    frame_creator()
    time.sleep(10)
    
    path='C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/video img/13.jpeg'
    in_im=cv2.imread(path)
    in_im_dis=cv2.resize(in_im,(540,600))
    cv2.imshow('original',in_im_dis)
    
    con_img=contrast_enhancement(path)
    sha_img=sharpness_enhancement(con_img)
    filters(sha_img)
    
    croped_img=cv2.imread('C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/13 i .png')
    croped_img=cv2.resize(croped_img,(240,300))
    cv2.imshow('croped image',croped_img)
    
    ocr_op=ocr('C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/13 i .png')
    print(ocr_op)
    cv2.waitKey(0)