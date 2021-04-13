#obs sobre ChainCode: O ChainCode é a representação do número. Nós extraímos a característica do número 1 usando chaincode. Existem diversas formas e extratores distintos. O chaincode é um tipo de extrator.  
#a manipulação da ChainCode está naquela função mais recente, a qual atualizei e "importei from utilsB import normalizeImage, verifyNeighborhood"
#na vertical do gráfico do ChainCode serão os 4 percursos onde irá ser percorrido para formar o 1. (aquele que aparece no print (0,1,2,3))


import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from utilsB import normalizeImage, verifyNeighborhood

ChainCode=[]
SignalLenght=[]
counter = 0
dim=(300,300)

path='./numbers/number1/' #aqui há uma pasta com várias imagens de números 1;
for r, d, f in os.walk(path): #um loop para analisar as pastas.
    for filename in f:
        
        image = cv2.imread(os.path.join(path,filename))
        image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)


        imageBin = 255 - image[:,:,0]

        newIm = np.zeros(np.shape(imageBin))
        kernel = np.ones((3,3), np.uint8)

        newIm = normalizeImage((imageBin>100)*1)
        imCopy = np.copy(newIm)
        imPlot = np.zeros(np.shape(image))
        imPlot[:,:,0] = imPlot[:,:,1] = imPlot[:,:,2] = imCopy

        newIm = cv2.dilate(newIm, kernel, iterations=1) - newIm
        newIm = cv2. resize(newIm, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('image',newIm)
        cv2.waitKey(0)
        max_xy = np.where(newIm == 255 )
        #print(max_xy[0][0], max_xy[1][0])

        #print (np.shape(newIm))

        newImRGB = np.zeros(np.shape(image))
        newImRGB[:,:,0] = newImRGB[:,:,1] = newImRGB[:,:,2] = newIm

        cv2.circle(newImRGB, (max_xy[1][0], max_xy[0][0]), int(3), (0, 0, 255),2)

        startPoint = (max_xy[0][0], max_xy[1][0])

        point = verifyNeighborhood(newIm, startPoint, 4,counter=counter,ChainCode=ChainCode,SignalLenght=SignalLenght)

        while(point!=startPoint):
            cv2.circle(imPlot, (point[1], point[0]), int(7), (0,0,255),4)
            cv2.imshow('Show Image', imPlot)
            cv2.waitKey(1)

            cv2.circle(imPlot,(point[1], point[0]), int(6), (0,255,255),6)
            point = verifyNeighborhood(newIm, point, 4, counter=counter, ChainCode=ChainCode, SignalLenght=SignalLenght)
        print (ChainCode)
        plt.plot(ChainCode)#para cada número 1 que eu achar na minha pasta vou mostrar de forma gráfica.
        plt.show()
        ChainCode= []

