import numpy as np
import cv2
import math

def Angle(x1,y1,x2,y2,x3,y3):
    A=(x2-x1,y2-y1)
    B=(x3-x1,y3-y1)

    dot_product=np.dot(A,B)
    dis_A=math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
    dis_B=math.sqrt((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1))
    radians=math.acos(dot_product/(dis_A*dis_B))
    degree=math.degrees(radians)
    return degree


def Caculate_angle(candidate):
    arm_left=0.0
    arm_right=0.0
    knee_left=0.0
    knee_right=0.0
    neck=0.0

    if candidate[12].visibility>=0.5 and candidate[11].visibility>=0.5:
        middle_shoulder_x=abs(candidate[12].x-candidate[11].x)/2
        middle_shoulder_x= middle_shoulder_x+candidate[12].x if candidate[12].x < candidate[11].x else middle_shoulder_x+candidate[11].x
        middle_shoulder_y=abs(candidate[12].y-candidate[11].y)/2
        middle_shoulder_y= middle_shoulder_y+candidate[12].y if candidate[12].y < candidate[11].y else middle_shoulder_y+candidate[11].y
        neck=Angle(middle_shoulder_x,middle_shoulder_y,candidate[0].x,candidate[0].y,middle_shoulder_x,0.0)

    if candidate[13].visibility>=0.5 and candidate[11].visibility>=0.5 and candidate[15].visibility>=0.5:
        arm_right=Angle(candidate[13].x,candidate[13].y,candidate[11].x,candidate[11].y,candidate[15].x,candidate[15].y)
    
    if candidate[14].visibility>=0.5 and candidate[12].visibility>=0.5 and candidate[16].visibility>=0.5:
        arm_left=Angle(candidate[14].x,candidate[14].y,candidate[12].x,candidate[12].y,candidate[16].x,candidate[16].y)
    
    if candidate[25].visibility>=0.5 and candidate[23].visibility>=0.5 and candidate[27].visibility>=0.5:
        knee_right=Angle(candidate[25].x,candidate[25].y,candidate[23].x,candidate[23].y,candidate[27].x,candidate[27].y)
    
    if candidate[26].visibility>=0.5 and candidate[24].visibility>=0.5 and candidate[28].visibility>=0.5:
        knee_left=Angle(candidate[26].x,candidate[26].y,candidate[24].x,candidate[24].y,candidate[28].x,candidate[28].y)
    
    result=(neck,arm_left,arm_right,knee_left,knee_right)
    print('Arm_left: '+str(arm_left)+'\n')
    print('Arm_right: '+str(arm_right)+'\n')
    print('knee_left: '+str(knee_left)+'\n')
    print('knee_right: '+str(knee_right)+'\n')
    with open('Angle.txt','a') as file:
        file.write('neck : '+str(neck)+'\n')
        file.write('Arm_left'+str(arm_left)+'\n')
        file.write('Arm_right'+str(arm_right)+'\n')
        file.write('knee_left'+str(knee_left)+'\n')
        file.write('knee_right'+str(knee_right)+'\n')

    return result
