import cv2
import os
import numpy as np


def canny_edge_detect(filename):

    folder='uploads'
    img = cv2.imread(os.path.join(folder,filename))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    canny = cv2.Canny(img, 100, 200)
    filename =  "edges" + filename
    cv2.imwrite(os.path.join(folder,filename),canny)
    return filename