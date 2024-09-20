from Angle import Angle
import cv2
import json
import math
import json

def touch1(candidate,array,image):
    #size = len(array)
    x26 = candidate[26].x
    x28 = candidate[28].x
    y26 = candidate[26].y
    y28 = candidate[28].y
    #------------------
    x25 = candidate[26].x
    x27 = candidate[27].x
    y25 = candidate[25].y
    y27 = candidate[27].y
    trp = candidate[23].x + candidate[24].x
    zrp = candidate[23].y + candidate[24].y
    fooxl = candidate[28].x
    fooyl = candidate[28].y
    fooxr = candidate[27].x
    fooyr = candidate[27].y 
    direction = 1  # if rig  gro m 1 , l 2
    ground_angle_r = int(abs(Angle(x28,y28,x26,y26,x28+10,y28)))
    ground_angle_l = int(abs(Angle(x27,y27,x25,y25,x27+10,y27)))
    if (direction == 1):
        if(85<=ground_angle_r<=95):
            #step+=1
            direction = 2
            #size+=1
            contact_angle_r = 180-int(Angle(fooxr,fooyr,trp,zrp,fooxl+30,fooyl))
            array.append(contact_angle_r)
            #if(85<=ground_angle_r<=95):
                #cv2.line(image, (int(candidate[23].x), int(candidate[23].y)), (int(candidate[24].x), int(candidate[24].y)), (255,255,0), 5)
                #cv2.line(image, (int(candidate[23].x), int(candidate[23].y)), (int(candidate[27].x), int(candidate[27].y)), (255,255,0), 5)
            with open('test_con.txt','a') as file:
                #array.append(contact_angle_l)
                file.write('angle'+str(contact_angle_r)+'\n')         
    else:
        if(85<=ground_angle_l<=95):
            #step+=1
            direction = 1
            #size+=1
            contact_angle_l = 180-int(Angle(fooxl,fooyl,trp,zrp,fooxl+30,fooyl))
            array.append(contact_angle_l)
            #if(85<=ground_angle_r<=95):
                #cv2.line(image, (int(candidate[23].x), int(candidate[23].y)), (int(candidate[24].x), int(candidate[24].y)), (255,255,0), 5)
                #cv2.line(image, (int(candidate[23].x), int(candidate[23].y)), (int(candidate[28].x), int(candidate[28].y)), (255,255,0), 5)
            with open('test_con.txt','a') as file:
                #array.append(contact_angle_l)
                file.write('angle'+str(contact_angle_l)+'\n')
    #with open('test_angle.txt','a') as file:
        #file.write('left angle'+str(ground_angle_r)+'\n')
        #file.write('right angle'+str(ground_angle_l)+'\n')
        #file.write('now step'+str(step)+'\n')
    return array
