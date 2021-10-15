from PIL import Image, ImageEnhance

#read the image
im = Image.open("sample-image.png")

#image brightness enhancer
enhancer = ImageEnhance.Contrast(im)

factor = 1 #gives original image
im_output = enhancer.enhance(factor)
im_output.save('original-image.png')

#factor = 0.5 #decrease constrast
#factor = 1.5 #increase constrast