import cv2
vidcap = cv2.VideoCapture('olcar.mp4')
success,image = vidcap.read()
count = 0
while success:
  fname='frame'+str(count)+'.jpg'
  path='C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/video img/'
  fpath=path+fname
  cv2.imwrite(fpath, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1