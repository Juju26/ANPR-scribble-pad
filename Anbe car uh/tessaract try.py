import pytesseract as ps
import cv2
image_Filename='C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/Anbe car uh/bmw white front.png'
# Read the file  using opencv and show the image
img=cv2.imread(image_Filename)
# cv2.imshow("Apparel Tag", img)
# cv2.waitKey(0)
#set the configuration for redaing text from image using pytesseract
#custom_config = r'--oem 1 --psm 8 -l eng'
text=ps.image_to_string(img)
print(text)