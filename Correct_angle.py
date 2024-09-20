from Angle import Caculate_angle
from Angle import Angle
import cv2
import json
def refresh_angle(candidate):
    middle_shoulder_x = abs(candidate[12].x - candidate[11].x) / 2
    middle_shoulder_x = int(middle_shoulder_x + candidate[12].x) if candidate[12].x < candidate[11].x else int(middle_shoulder_x + candidate[11].x)
    middle_shoulder_y = abs(candidate[12].y - candidate[11].y) / 2
    middle_shoulder_y = int(middle_shoulder_y + candidate[12].y) if candidate[12].y < candidate[11].y else int(middle_shoulder_y + candidate[11].y)
    degree = Angle(middle_shoulder_x,middle_shoulder_y,candidate[0].x,candidate[0].y,middle_shoulder_x+10,middle_shoulder_y)  
    #right = 1?
    #print("dergee___ = ",degree)
    if (degree<90):
        return 1
    else:
        return 0 
    
def draw_correct_angle(flag,candidate,image):
    if flag[0]:
        middle_shoulder_x = abs(candidate[12].x - candidate[11].x) / 2
        middle_shoulder_x = int(middle_shoulder_x + candidate[12].x) if candidate[12].x < candidate[11].x else int(middle_shoulder_x + candidate[11].x)
        middle_shoulder_y = abs(candidate[12].y - candidate[11].y) / 2
        middle_shoulder_y = int(middle_shoulder_y + candidate[12].y) if candidate[12].y < candidate[11].y else int(middle_shoulder_y + candidate[11].y)
        cv2.line(image, (int(candidate[0].x), int(candidate[0].y)), (middle_shoulder_x, middle_shoulder_y), (255, 255, 255), 5)#123
    if flag[1]:
        cv2.line(image, (int(candidate[23].x), int(candidate[23].y)), (int(candidate[25].x), int(candidate[25].y)), (0, 0, 255), 5)
        cv2.line(image, (int(candidate[25].x), int(candidate[25].y)), (int(candidate[27].x), int(candidate[27].y)), (0, 0, 255), 5)
        
    if flag[2]:
        cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[26].x), int(candidate[26].y)), (0, 0, 255), 5)
        cv2.line(image, (int(candidate[26].x), int(candidate[26].y)), (int(candidate[28].x), int(candidate[28].y)), (0, 0, 255), 5)

    if flag[3]:
        cv2.line(image, (int(candidate[12].x), int(candidate[12].y)), (int(candidate[14].x), int(candidate[14].y)), (0, 0, 255), 5)
        cv2.line(image, (int(candidate[14].x), int(candidate[14].y)), (int(candidate[16].x), int(candidate[16].y)), (0, 0, 255), 5)
    if flag[4]:
        cv2.line(image, (int(candidate[11].x), int(candidate[11].y)), (int(candidate[13].x), int(candidate[13].y)), (0, 0, 255), 5)
        cv2.line(image, (int(candidate[13].x), int(candidate[13].y)), (int(candidate[15].x), int(candidate[15].y)), (0, 0, 255), 5)
    return image




def check_angle(candidate,config,image):
    neck,arm_left,arm_right,knee_left,knee_right = Caculate_angle(candidate)
    flag_neck=False
    flag_armR=False
    flag_armL=False
    flag_kneeL=False
    flag_kneeR=False

    deduction=0
    
    if neck>=max(config['Neck']) or neck<=min(config['Neck']):
        flag_neck=True
        deduction+=config['deduction']*config['Neck_weight']
    if arm_left>=max(config['Arm_left']) or arm_left<=min(config['Arm_left']):
        flag_armL=True
        deduction+=config['deduction']*config['Arm_left_weight']
    if arm_right>=max(config['Arm_right']) or arm_right<=min(config['Arm_right']):
        flag_armR=True
        deduction+=config['deduction']*config['Arm_right_weight']
    if knee_left>=max(config['Knee_left']) or knee_left<=min(config['Knee_left']):
        flag_kneeL=True
        deduction+=config['deduction']*config['Knee_left_weight']
    if knee_right>=max(config['Knee_right']) or knee_right<=min(config['Knee_right']):
        flag_kneeR=True
        deduction+=config['deduction']*config['Knee_right_weight']
    flag=[flag_neck,flag_kneeR,flag_kneeL,flag_armL,flag_armR]
    if any(flag):
        return (draw_correct_angle(flag,candidate,image),deduction)
    return (image,deduction)


def correct_angle(candidate,image):
    with open('config.json') as file:
        config=json.load(file)
    return check_angle(candidate,config,image)
