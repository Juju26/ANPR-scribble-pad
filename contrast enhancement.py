from PIL import Image, ImageEnhance

#read the image
im = Image.open("C:/Users/Asus/OneDrive/Desktop/ANPR scribble pad/Anbe car uh/tata sus.jpeg")

#image brightness enhancer
enhancer = ImageEnhance.Contrast(im)

factor = 1.5 #gives original image
im_output = enhancer.enhance(factor)
im_output.save('op.jpeg')

#factor = 0.5 #decrease constrast
#factor = 1.5 #increase constrast