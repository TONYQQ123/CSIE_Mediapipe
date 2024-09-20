from Angle import Angle
import cv2
import json
import math
import json
def writepy(candidate,array):
    center = candidate[24].y + candidate[23].y
    array.append(center)
    with open('pydraw.txt','a') as file:
                #array.append(contact_angle_l)
        file.write(str(center)+'\n')  
    return array
