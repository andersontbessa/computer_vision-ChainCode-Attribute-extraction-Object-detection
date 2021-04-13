
from skimage.feature import greycomatrix, greycoprops
from skimage.feature import local_binary_pattern

import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import time, threading
import function_q3 as gV
from function_q3 import normalizeImage

new_width = 400
new_height = 400



cap = cv2.VideoCapture(1)

fileLBP = open('analyze_video', 'w')

#plotagem.
plt.style.use("ggplot")
(fig, ax) = plt.subplots()
fig.suptitle("Local Binary Patterns")
plt.ylabel("% of Pixels")
plt.xlabel("LBP pixel bucket")

plt.ion()
ret, frame = cap.read()

#abrir um vídeo para análise.
cap = cv2.VideoCapture('car.mp4')

#cv2.selectROI: Seleciona uma caixa delimitadora ou uma região retangular de interesse (ROI) em uma imagem.
selected = [0,0]
while selected == [0,0]:
	_, frame = cap.read()
	r = cv2.selectROI(frame)
	selected = [r[1],r[0]]

cv2.destroyAllWindows()

cv2.namedWindow('tracker')
gV.selRoi = 0

gV.top_left= [r[1],r[0]]
gV.bottom_right = [r[1] + r[3],r[0] + r[2]]
gV.first_time = 1
print(gV.top_left,gV.bottom_right)

ts = [ gV.bottom_right[1] - gV.top_left[1], gV.bottom_right[0] - gV.top_left[0]]
print(ts,ts[0]/2)
count = 0

while(cap.isOpened()):
    ret, frame = cap.read()

    ImageGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    roi = frame[gV.top_left[0]:gV.bottom_right[0], gV.top_left[1]:gV.bottom_right[1]]  # selecting roi

    sum = np.sum(roi) #aqui será a soma de todos os pixels.     
    x = [1, 2, 3]

    y = [sum, sum, sum ]

    plt.cla()
    plt.plot(x, y)
    # save figure
    plt.pause(0.001)
    
    cv2.imshow("LBP_Image", roi )
    cv2.waitKey(1)


cap.release()

