import cv2
import numpy as np

def resize_image(img, channel=3):
    gray_img = img[:,:,channel]
    bin_img = gray_img / 25
    bin_img = cv2.resize(bin_img, (32, 32))
    img_32X32 = bin_img > 0
    img_32X32 = img_32X32.astype(int)
    img_1X1024 = np.reshape(img_32X32, (1, 1024)) 
    return img_1X1024  
