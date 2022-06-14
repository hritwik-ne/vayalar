from statistics import mode
import sys
import functools
import numpy as np
import matplotlib.pyplot as mlt
import cv2
import algo.model as am

def compare_rect(rect1, rect2):
    if abs(rect1[1] - rect2[1]) > 10:
        return rect1[1] - rect2[1]
    else:
        return rect1[0] - rect2[0]

def segm(img):

    #### Gray, Blurring and thresholding
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,45,15)

    #### Connected Component analaysis
    _, labels = cv2.connectedComponents(thresh)
    mask = np.zeros(thresh.shape,dtype = "uint8")

    #### Setting lower and upperbound for chars
    total_pixels = img.shape[0] * img.shape[1]
    lower = total_pixels 
    upper = total_pixels 
    for i,label in enumerate(np.unique(labels)):
        if label==0:
            continue
        labelMask = np.zeros(thresh.shape,dtype="uint8")
        labelMask[labels==label] = 255
        numPixels = cv2.countNonZero(labelMask)
        mask = cv2.add(mask, labelMask)

    #### Finding Contours
    cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]    
    boundingBoxes = sorted(boundingBoxes, key=functools.cmp_to_key(compare_rect) )

    crop_characters=[]
    for rect in boundingBoxes:
        (x,y,w,h) = rect
        ratio = h/w
        cv2.rectangle(img.copy(), (x, y), (x + w, y + h), (0, 255,0), 2)
        curr_num = mask[y:y+h,x:x+w]
        crop_characters.append(curr_num)
                
    print("Detect {} letters...".format(len(crop_characters))) 
    return crop_characters
    

def recognise_text(img_path, mdl):
    image = cv2.imread(img_path)
    word = []
    images = segm(image)
    n = len(images)
    for i in range(n):
        result = mdl.test(images[i])
        word.append(int(result))
    return word

def init(model_path):
    mdl = am.Model(model_path)
    return mdl

if __name__ == '__main__':
    model_path = 'res/model_v3.sav'
    img_path = 'data/sample.png'
    mdl = am.Model(model_path)
    result = recognise_text(img_path, mdl)
    print(result)
