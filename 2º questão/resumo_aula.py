import numpy as np
import cv2
import matplotlib.pyplot as plt
from functions_q2 import normalizeImage, writeElementInDataset

from skimage.feature import greycomatrix, greycoprops
from skimage.feature import local_binary_pattern
import os
import time, threading


#o HU pega o objeto e vai ver medida de similaridade desse objeto.
def HU_FE(image): #passa um dataset em que quero analisar, a retornar um array para montar um dataset para fazer as analises estatísticas.
    moments = cv2.moments(image.astype(np.float64))
    return np.asarray(cv2.HuMoments(moments).flatten()) #o np.asarray retorna um array bem definido

def LBP_FE(image): #o LBP e o GLCM são extratores que normalmente são usados para analisar texturas, se quero ver se é suave, rugoso etc.
    lbp_image = local_binary_pattern(image, 256, 1, "uniform") #o 256 é o teto da relação de bytes. Conforme vai diminuindo esse valor, vai acabar perdendo valor. Acaba tendo um gráfico mais amortizado.
    return np.histogram(lbp_image.ravel(), bins=256)

def GLCM_FE(image):
    glcm= greycomatrix(image, [1], [0], 256, symmetric=True, normed=True)
    xs=[]
    xs.append(greycoprops(glcm, 'dissimilarity')[0,0])
    xs.append(greycoprops(glcm, 'correlation')[0,0])
    xs.append(greycoprops(glcm, 'homogeneity')[0,0])
    xs.append(greycoprops(glcm, 'ASM')[0,0])
    xs.append(greycoprops(glcm, 'energy')[0,0])
    return np.asarray(xs)

#def normalizeImage

#def writeElementInDataset

cap = cv2.VideoCapture(0)


fileLBP = open('FE_LBP.dat', 'w')

plt.style.use("ggplot")
(fig,ax) = plt.subplots()
fig.suptitle("Local Binary Patterns")
plt.ylabel("% of pixels")
plt.xlabel("LBP pixel bucket")

plt.ion()

while(cap.isOpened()):
    ret, frame = cap.read()

    new_width = 300
    new_height = 300

    gray_origin = cv2.resize(frame, (new_width, new_height), interpolation = cv2.INTER_AREA)

    
    features = local_binary_pattern(gray_origin[:,:,1], 128, 2, method="uniform")

    cv2.imshow("LBP_Image", features.astype("uint8"))
    cv2.imshow("Original Image", frame)

    cv2.waitKey(1)
    plt.cla()
    #ax.hist(features.ravel(), normed=True, bins=64, range=(0,64))
    ax.set_xlim([0,64]) #onde vai aparecer no gráfico.
    ax.set_ylim([0,0.030])

    plt.pause(0.1)



    
