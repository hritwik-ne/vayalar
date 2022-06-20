import pickle
from PIL import Image
import numpy as np
import cv2
from skimage.transform import resize

DEBUG = False

class Model():
    def __init__(self, model_path):
        self.model = pickle.load(open('res/model_v3.sav', 'rb'))
    
    def test(self, image):
        image_rz = cv2.resize(image, (86,86))
        image_rz_bin = np.array(image_rz)/255
        X_test = np.reshape(image_rz_bin, (1,7396))
        result = self.model.predict(X_test)
        
        if DEBUG:
            print(result)
            print(X_test.shape)
            print(X_test)
        
        return(result)

    
    