import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
images = []
edges = []
for elem in os.listdir():
    if elem.split('.')[-1]=='jpg':
        images.append(elem)

for elem in images:
    image = elem
    img = cv2.imread(image)
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_gray_blur=cv2.GaussianBlur(img_gray,(15,15),0)
    canny_edges=cv2.Canny(img_gray_blur,10,70)
    ret, mask=cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
    cv2.imwrite('edg_'+elem,mask)
    edges.append('edg_'+elem)
    
for i in range(len(edges)):
    mask = cv2.imread(edges[i])
    img = cv2.imread(images[i])

    h1, w1 = img.shape[:2]
    h2, w2 = mask.shape[:2]

    #create empty matrix
    vis = np.zeros((max(h1, h2), w1+w2,3), np.uint8)

    #combine 2 images
    vis[:h1, :w1,:3] = img
    vis[:h2, w1:w1+w2,:3] = mask
    
    cv2.imwrite('doub_'+images[i],vis)
