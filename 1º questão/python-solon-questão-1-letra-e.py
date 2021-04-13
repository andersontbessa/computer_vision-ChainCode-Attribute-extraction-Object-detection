import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from utilsC import normalizeImage, verifyNeighborhood
from collections import Counter
from recover import recoverImg
import random
from blackBoxes2 import Normalize

signals= []
reducedSignals = []
ChainCode = []
SignalLenght = []
counter = 0
imgCounter = 1;
dim = (600,600) #600,600 chega mais próximo de uma imagem real do número 1, tendo em vista todas as figuras 1.
path='./numbers/number1/'

#a moda vai contar na lista a frequência para cada número.
def most_frequent(List):
    occurence_count = Counter(List)
    rand=0
    if occurence_count.most_common(1)[0][1] <=2:
        rand=random.randint(0,1)
    return occurence_count.most_common(1)[0][0]

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

        newIm = cv2.erode(newIm, kernel, iterations=1)

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
            
            #cv2.circle(imPlot, (point[1], point[0]), int(3), (0, 0, 255), 4)
            #cv2.imshow('image', imPlot)
            #cv2.waitKey(1)

            # cv2.circle(imPlot, (point[1], point[0]), int(3), (0, 255, 255), 6)
            point = verifyNeighborhood(newIm, point, 4, counter=counter, ChainCode=ChainCode, SignalLenght=SignalLenght)


        plt.subplot(imgLength, 1, imgCounter)
        plt.plot(ChainCode)
    
        imgCounter = imgCounter + 1
        ChainCode = []

    smaller = 9999
    for number in signals:
        numberLenght = len(number)
        #print ("tamanho da lista",len(number) ) #teste
        if numberLenght < smaller:
            smaller = numberLenght
            print ("smaller",smaller)

    from scipy.ndimage import interpolation

    for number in signals:
        diff = len(number) - smaller
        if diff != 0 :
            newSignal = Normalize(number,smaller)#o algorimo blackBoxNormalization vai pegar códigos grande e reduzir para códigos menores;
            reducedSignals.append(newSignal)#black
    meanSignal = np.mean(reducedSignals, axis=0)

    for b in range(len(meanSignal)):
        meanSignal[b] = np.int(meanSignal[b])
    

    res = dict(Counter(meanSignal))
    recoveredImage=np.zeros((500,500))

    initialPoint = (100,170)
    nextPoint = initialPoint

    #most_frequent
    reducedSignals= np.array(reducedSignals)
    print(np.shape(reducedSignals))

    for indx in range (smaller):
        listIndx = reducedSignals[:,indx]

        npArray = np.array([b for elem in listIndx])

        value = most_frequent(reducedSignals[:,indx])

        nextPoint = recoverImg(recoveredImage,nextPoint, value)

        cv.imshow('meanImage, recoveredImage')

        cv2.waitKey(1)

cv2.waitKey(0)

