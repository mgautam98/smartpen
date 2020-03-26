import cv2
import os
import numpy as np

edges = []

def get_closest_edge(filename, X, Y):
    return (X,Y)

def canny_edge_detect(filename):

    folder='uploads'
    img = cv2.imread(os.path.join(folder,filename))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    canny = cv2.Canny(img, 100, 200)
    filename =  "edges" + filename
    cv2.imwrite(os.path.join(folder,filename),canny)

    edges.clear()
    for ix in range(canny.shape[0]):
        for iy in range(canny.shape[1]):
            if canny[ix][iy]>128:
                edges.append([ix,iy])

    return [filename, edges]