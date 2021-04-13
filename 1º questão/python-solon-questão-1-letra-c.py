import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from utilsC import normalizeImage, verifyNeighborhood
from collections import Counter
from recover import recoverImg 


ChainCode = []
SignalLenght = []
counter = 0
imgCounter = 1;
dim = (300,300)
path='./numbers/number1/'


for r, d, f in os.walk(path):
    imgLength = len(f)
    for filename in f:

        image = cv2.imread(os.path.join(path,filename))
        image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

        imageBin = 255 - image[:, :, 0]

        newIm = np.zeros(np.shape(imageBin))
        kernel = np.ones((3, 3), np.uint8)

        newIm = normalizeImage((imageBin > 100) * 1)
        imCopy = np.copy(newIm)

        imPlot = np.zeros(np.shape(image))
        imPlot[:, :, 0] = imPlot[:, :, 1] = imPlot[:, :, 2] = imCopy

        newIm = cv2.dilate(newIm, kernel, iterations=1) - newIm
        newIm = cv2.resize(newIm, dim, interpolation=cv2.INTER_AREA)

        max_xy = np.where(newIm == 255)
        # print(max_xy[0][0] , max_xy[1][0])

        print(np.shape(newIm))
        newImRGB = np.zeros(np.shape(image))
        newImRGB[:, :, 0] = newImRGB[:, :, 1] = newImRGB[:, :, 2] = newIm

        cv2.circle(newImRGB, (max_xy[1][0], max_xy[0][0]), int(3), (0, 0, 255), 2)

        startPoint = (max_xy[0][0], max_xy[1][0])

        point = verifyNeighborhood(newIm, startPoint, 4,counter=counter,ChainCode=ChainCode,SignalLenght=SignalLenght)

        while (point != startPoint):
            
            cv2.circle(imPlot, (point[1], point[0]), int(3), (0, 0, 255), 4)
            cv2.imshow('image', imPlot)
            cv2.waitKey(1)

            # cv2.circle(imPlot, (point[1], point[0]), int(3), (0, 255, 255), 6)
            point = verifyNeighborhood(newIm, point, 4, counter=counter, ChainCode=ChainCode, SignalLenght=SignalLenght)


        #para fazer uma cópia de cada imagem 1.
        res = dict(Counter(  ChainCode  ))
        recoveredImage = np.zeros((int(res[0]*1.2) ,int((res[1]+res[3])*1.2) ))

        initialPoint = (30,res[1])
        nextPoint = initialPoint
        for value in ChainCode:
            nextPoint = recoverImg(recoveredImage,nextPoint,value)
            cv2.imshow('imageRecovered', recoveredImage)
            cv2.waitKey(1)

        plt.subplot(imgLength, 1, imgCounter)
        plt.plot(ChainCode)
        imgCounter = imgCounter + 1
        ChainCode = []

    plt.show()





cv2.imshow('image', imPlot)
cv2.waitKey(0)
