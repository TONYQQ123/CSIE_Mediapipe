from Angle import Angle
import cv2
import json
import math
import json

def ground(candidate,array,image,step):
    heavy_point = int(candidate[24].y) + int(candidate[24].y)
    array.append(heavy_point)
    #print("heavy point = ",heavy_point)
    #print(heavy_point)
    #if(len(array)>10):
        #print(heavy_point[0],heavy_point[1])
    pos = len(array)-1
    if (pos>1):
        if(array[pos]>array[pos-1] and array[pos-2]> array[pos-1]):
            step+=1
    #print("now image =",len(array))
    #print("now step",step)
    #with open('abc.txt','a') as file:
        #file.write('the program sta222rt'+'\n')
    return array,step