import easyocr
import os
import glob

#filenames='C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/Anbe car uh/bmw white front.png'
#filenames='C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/Anbe car uh/tata sus.jpeg'
#filenames='C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/Anbe car uh/blur img.jpeg'
filenames='C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/Anbe car uh/2cars.jpeg'

with open(filenames,'r') as fi:
    res_list=[]
    read=easyocr.Reader(['en'])
    result=read.readtext(filenames)
    for i in range(len(result)):    
        p=[]
        p.append(result[i][1])
        res_list.append(''.join(i for i in p))
    print(res_list)