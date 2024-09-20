from Angle import Angle
import cv2

def stoop_angle(candidate, array, image):
    angle_left = int(abs(Angle(candidate[27].x, candidate[27].y, candidate[25].x, candidate[25].y, (candidate[27].x)+10, candidate[27].y)))
    angle_right = int(abs(Angle(candidate[28].x, candidate[28].y, candidate[26].x, candidate[26].y, (candidate[28].x)+10, candidate[28].y)))
    judge_r = (candidate[18].x)-(candidate[14].x)
    judge_l = (candidate[17].x)-(candidate[13].x)
    flag = 0
    if(judge_r < 0 and judge_l < 0): # 往左跑
        if(85<=angle_left<=95):  # 左腳跟著地瞬間
            stoop = abs(90.0 - Angle(candidate[24].x, candidate[24].y, candidate[12].x, candidate[12].y, (candidate[24].x)-10, candidate[24].y))
            array.append(stoop)
            if(stoop<=80.0):
                cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[12].x), int(candidate[12].y)), (255, 0, 0), 20)
                cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[24].x)-300, int(candidate[24].y)), (255, 0, 0), 20)
                flag = 1

        elif(85<=angle_right<=95):  # 右腳跟著地瞬間
            stoop = abs(90.0 - Angle(candidate[24].x, candidate[24].y, candidate[12].x, candidate[12].y, (candidate[24].x)-10, candidate[24].y))
            array.append(stoop)
            if(stoop<=80.0):
                cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[12].x), int(candidate[12].y)), (255, 0, 0), 20)
                cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[24].x)-300, int(candidate[24].y)), (255, 0, 0), 20)
                flag = 1

    elif(judge_r > 0 and judge_l > 0): # 往右跑
        if(85<=angle_left<=95):  # 左腳跟著地瞬間
            stoop = abs(90.0 - Angle(candidate[24].x, candidate[24].y, candidate[12].x, candidate[12].y, (candidate[24].x)-10, candidate[24].y))
            array.append(stoop)
            if(stoop<=80.0):
                cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[12].x), int(candidate[12].y)), (255, 0, 0), 20)
                cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[24].x)+300, int(candidate[24].y)), (255, 0, 0), 20)
                flag = 1

        elif(85<=angle_right<=95):  # 右腳跟著地瞬間
            stoop = abs(90.0 - Angle(candidate[24].x, candidate[24].y, candidate[12].x, candidate[12].y, (candidate[24].x)-10, candidate[24].y))
            array.append(stoop)
            if(stoop<=80.0):
                cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[12].x), int(candidate[12].y)), (255, 0, 0), 20)
                cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[24].x)+300, int(candidate[24].y)), (255, 0, 0), 20)
                flag = 1

    return array, flag
