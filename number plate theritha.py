import easyocr
import os
import glob

#filenames='C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/Anbe car uh/bmw white front.png'
#filenames='C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/Anbe car uh/tata sus.jpeg'
#filenames='C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/Anbe car uh/blur img.jpeg'
# filenames='C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/Anbe car uh/jpgs'
# for filename in glob.glob(os.path.join(filenames, '*.jpg')):
#     with open(os.path.join(filenames, filename),'r') as fi:
#         res_list=[]
#         read=easyocr.Reader(['en'])
#         result=read.readtext(filenames) 
#         for i in range(len(result)):    
#             p=[]
#             p.append(result[i][1])
#             res_list.append(''.join(i for i in p))
#             print(res_list)
#         print('hi')

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
    print(res_list)