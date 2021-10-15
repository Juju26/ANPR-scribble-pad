# Steps to Sharpen Image using PIL
# To adjust image sharpness using Python Pillow,

# Read the image using Image.open().
# Create ImageEnhance.Sharpness() enhancer for the image.
# Enhance the image sharpness using enhance() method, by the required factor.
# By adjusting the factor you can sharpen or blur the image.

# While a factor of 1 gives original image. factor>1 sharpens the image while factor<1 blurs the image


from PIL import Image, ImageEnhance

im = Image.open("original-image.png")

enhancer = ImageEnhance.Sharpness(im)

factor = 1
im_s_1 = enhancer.enhance(factor)
im_s_1.save('original-image-1.png')

factor = 0.05
im_s_1 = enhancer.enhance(factor)
im_s_1.save('blurred-image.png')

factor = 2
im_s_1 = enhancer.enhance(factor)
im_s_1.save('sharpened-image.png')