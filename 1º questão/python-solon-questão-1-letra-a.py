import numpy as np
import cv2
import matplotlib.pyplot as plt

def verifyNeighborhood(image, point, connectivity): #essa função vai ver o grau de conectividade que estou buscando, se é o de 4 dimensões ou o de 8.  Nesse caso estamos usando o de 4.
    if connectivity == 4:
       # print(point)
        if image [point[0]-1, point[1]] == 255: #se nesse ponto tiver o valor 255,
            image [point[0]-1, point[1]] = 0 #aí atribuo a esse ponto o valor 0.
            #print('0') #zero será a direção para cima.
            return (point[0]-1, point[1])
        
        elif image [point[0], point[1]+1] == 255: #o point[1]+1] quer dizer que vai para direita.
            image [point[0], point[1]+1] = 0
            #print('1')#printa 1 se for para direita.
            return (point[0], point[1]+1)

        elif image [point[0]+1, point[1]] == 255: #direção para baixo.
            image [point[0]+1, point[1]] = 0
            #print('2')
            return (point[0]+1, point[1])

        elif image [point[0], point[1]-1] == 255: ##direção para esquerda.
            image [point[0], point[1]-1] = 0
            #print('3')
            return (point[0], point[1]-1)


        else:
            print('none') # para caso não rodar nenhuma condição acima.

    else:
        return point

def normalizeImage(v): #função para normalizar a imagem entre zeros e uns.
    v = (v-v.min())/(v.max()-v.min())
    result= (v*255).astype(np.uint8)
    return result

#a partir daqui começa de fato o código. Acima são funções que irei usar nos próximos exercícios.

image = cv2.imread('1_5.jpg')

imageBin = 255 - image[:,:,0] #converte em uma imagem binária. Pega um canal dentre os 3 canais RGB. (exploco mais baixo)

newIm = np.zeros(np.shape(imageBin))
kernel = np.ones((3,3), np.uint8)

newIm = normalizeImage((imageBin>100)*1)#tendo em vista a função normalizeImage, a imagem tinha zeros e uns, no momento que normalizo vai ter 0, 255.
imCopy = np.copy(newIm)
imPlot = np.zeros(np.shape(image))
imPlot[:,:,0] = imPlot[:,:,1] = imPlot[:,:,2] = imCopy

newIm = cv2.dilate(newIm, kernel, iterations=1) - newIm
cv2.imshow('image',imPlot)
cv2.waitKey(0)
max_xy = np.where(newIm == 255 ) #a função np.where vai encontrar valores iguais a newIm == 255 e retorna uma lista com suas localizações. 
#print(max_xy[0][0], max_xy[1][0]) #logo, nessa lista de  localização max_xy retornou a posição mais alta.
#print (max_xy)

newImRGB = np.zeros(np.shape(image)) #cria uma cópia da imagem original, com o msm tamanho.
#newImRGB[:,:,0] = newImRGB[:,:,1] = newImRGB[:,:,2] = newIm #isso aqui é só para fins didáticos.#dúvida.

cv2.circle(newImRGB, (max_xy[1][0], max_xy[0][0]), int(3), (0, 0, 255),2)#aqui plota um círculo no ponto inicial.

startPoint = (max_xy[0][0], max_xy[1][0])#aqui eu digo qual é o primeiro ponto inicial, que foi o que eu achei acima com a função np.where.

point = verifyNeighborhood(newIm, startPoint, 4)#aqui fará o processo de verificação de vizinhança.

#obs:o círculo azul indica o ponto que está sendo verificado atualmente, o roxa e que já foi verificado.
while(point!=startPoint): #enquanto meu ponto (point) for diferente do ponto inicial(startPoint), ou seja, vai encontrando alguns pontos e plotando todos os eu já passei, é a questão do círculo azul e o resto roxo.
    cv2.circle(imPlot, (point[1], point[0]), int(7), (255,255,0),4) #pontos do círculo azul.
    cv2.imshow('Show Image', imPlot)
    cv2.waitKey(1)

    cv2.circle(imPlot,(point[1], point[0]), int(6), (255,0,255),6)#pontos do círculo roxo.
    
    point = verifyNeighborhood(newIm,point,4)
cv2.imshow('image', imPlot)
cv2.waitKey(0)
#o ponto max_xy[1][0], max_xy[0][0] é onde vai iniciar a plotagem do círculo e o ponto max_xy[0][0], max_xy[1][0] é o próximo ponto que vem depois do ponto do círculo?
#resposta:Na verdade são o mesmo ponto, ocorre que pra fins de plotagem o opencv inverte algumas ordens. Como se primeiro ele precisasse da coluna e depois linha, mas a coordenada na matriz é linha e coluna. O caso dele ser vermelho indica o ponto que está sendo verificado atualmente, o amarelo e que já foi verificado.

#SOBRE O imageBin = 255 - image[:,:,0]. --->

#import cv2
#import numpy as np
#img = cv2.imread("image.jpg")

#usa assim ao invés de separar os canais de cores na função split
#b = img[:,:,0]
#g = img[:,:,1]
#r = img[:,:,2]


#aqui pega o primeiro canal de cor e subtrai tonalidade 255 
#primeiraTonalidade = 255 - img[:,:,0]
