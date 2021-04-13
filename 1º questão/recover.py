import numpy as np
import cv2
import matplotlib.pyplot as plt

def recoverImg(image, point, value):

        if value == 0:
            image[point[0]-1,point[1]] = 255
            return (point[0] - 1, point[1])

        elif value == 1:
            image[point[0],point[1]+1] = 255
            return (point[0], point[1] + 1)

        elif  value == 2:
            image[point[0]+1,point[1]] = 255
            return (point[0] + 1, point[1])

        elif  value == 3:
            image[point[0],point[1]-1] = 255
            return (point[0], point[1] - 1)

        return 'null'
