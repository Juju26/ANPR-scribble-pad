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
    #cv2.imshow(filenames)
    with open(filenames,'r') as fi:
        res_list=[]
        read=easyocr.Reader(['en'])
        result=read.readtext(filenames)
        for i in range(len(result)):    
            p=[]
            p.append(result[i][1])
            res_list.append(''.join(i for i in p))   
    return res_list

def filters():
    return

def file_writer():
    return 

if __name__=="__main__":
    path='C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/Anbe car uh/bmw white front.png'
    in_im=cv2.imread(path)
    in_im_dis=cv2.resize(in_im,(540,600))
    cv2.imshow('original',in_im_dis)
    con_img=contrast_enhancement(path)
    sha_img=sharpness_enhancement(con_img)
    ocr_op=ocr(sha_img)
    print(ocr_op)
   

    