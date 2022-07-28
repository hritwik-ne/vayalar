import cv2
import numpy as np
import matplotlib.pyplot as plt
import joblib

def recog(img):
    clf = joblib.load(open('res/model_v3.sav', 'rb'))
    img_cv2 = cv2.imread(f'{img}')
    img_cv2 = img_cv2[:,:,2]
    # print(img_cv2.shape)
    pix = np.reshape(img_cv2    ,(1,7396))
    return(clf.predict(pix))