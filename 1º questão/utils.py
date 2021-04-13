import numpy as np
import cv2
import matplotlib.pyplot as plt

def verifyNeighborhood(image, point, connectivity):
    if connectivity == 4:
        print(point)
        if image [point[0]-1, point[1]] == 255:
            image [point[0]-1, point[1]] = 0
            print('0')
            return (point[0]-1, point[1])
        
        elif image [point[0], point[1]+1] == 255:
            image [point[0], point[1]+1] = 0
            print('1')
            return (point[0], point[1]+1)

        elif image [point[0]+1, point[1]] == 255:
            image [point[0]+1, point[1]] = 0
            print('2')
            return (point[0]+1, point[1])

        elif image [point[0], point[1]-1] == 255:
            image [point[0], point[1]-1] = 0
            print('3')
            return (point[0], point[1]-1)


        else:
            print('none')

    else:
        return point

def normalizeImage(v):
    v = (v-v.min())/(v.max()-v.min())
    result= (v*255).astype(np.uint8)
    return result
