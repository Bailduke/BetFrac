"""
Code made by: BetFrac team
This code has been made for binarizing images in orther to
calculate it fractal dimension using "ImageJ"
"""
import cv2
import numpy as np

name = str(input("Introduce the name of the image with its exstension: "))
image = cv2.imread(name,0) # ,0 in gray scale

def output(image, name):
    image = np.array(image, dtype=float)/float(255) #we convert it to floats between (0,1)
    shape = image.shape  #this way works 2d and 3d
    height = int(shape[0] / 4)
    width = int(shape[1] / 4)
    image2 = cv2.resize(image, (width, height))
    cv2.namedWindow(name)
    cv2.imshow(name, image2)
    cv2.waitKey(0)

def equalize(image, p=2.15): #"p" = percentil
    in_min = np.percentile(image, 3*p)
    in_max = np.percentile(image, 100-p)
    out_min = 0.0  
    out_max = 255.0
    out = image - in_min
    out = out*((out_max - out_min) / (in_max - in_min))
    out =out + in_min
    #we set <0 to 0 and >255 to 255
    out [out <0] = 0 
    out [out >255] = 255
    return out

def binarize(image,u=0.8):
    u=u*image.max()
    image [image <u] = 0 
    image [image >=u] = 255
    return image

output(image, 'Original')
equalizedImg=equalize(image)
output(equalizedImg, 'constrasted')
image=binarize(equalizedImg)
output(image, 'binarized')

#cut the img
imageOut = image[600:2648,1050:3098]
output(imageOut, 'cut')

cv2.destroyAllWindows()
cv2.imwrite('BiN.png',imageOut)

cv2.imwrite('binarized.png',image)
