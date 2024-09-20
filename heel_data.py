from Angle import Angle
import cv2

#direction_camear == 0

def heel(candidate, L_heel, R_heel, waist, shoulder, image, direction_camear):
    L_heel.append(candidate[29].y)
    R_heel.append(candidate[30].y)
    waist.append(candidate[24])
    shoulder.append(candidate[12])
    i = len(L_heel)
    j = len(R_heel)
    
    judge_r = (candidate[18].x)-(candidate[14].x)
    judge_l = (candidate[17].x)-(candidate[13].x)
    #judge_r < 0 and judge_l < 0
    #judge_r > 0 and judge_l > 0
    if(i >= 2 and j >= 2 and judge_r < 0 and judge_l < 0): #往左跑
        if(abs(L_heel[i-2]-L_heel[i-1]) < 2):
            #print(11111111111)
            if(abs(90.0 - Angle(candidate[24].x, candidate[24].y, candidate[12].x, candidate[12].y, (candidate[24].x) - 10, candidate[24].y)) <= 80.0):
                cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[12].x), int(candidate[12].y)), (255, 0, 0), 20)
                cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[24].x)-300, int(candidate[24].y)), (255, 0, 0), 20)
                #print(11111111111111)
                #count = count + 1
    	        
        elif(abs(R_heel[j-2]-R_heel[j-1]) < 2):
            #print(22222222)
            if(abs(90.0 - Angle(candidate[24].x, candidate[24].y, candidate[12].x, candidate[12].y, (candidate[24].x) - 10, candidate[24].y)) <= 80.0):
                cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[12].x), int(candidate[12].y)), (255, 0, 0), 20)
                cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[24].x)-300, int(candidate[24].y)), (255, 0, 0), 20)
                #print(00000000000000)
                #count = count + 1

    	        
    elif(i >= 2 and j >= 2 and judge_r > 0 and judge_l > 0): #往右跑
        if(abs(L_heel[i-2]-L_heel[i-1]) < 2):
            #print(11111111111)
            if(abs(90.0 - Angle(candidate[24].x, candidate[24].y, candidate[12].x, candidate[12].y, (candidate[24].x) - 10, candidate[24].y)) <= 80.0):
                cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[12].x), int(candidate[12].y)), (255, 0, 0), 20)
                cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[24].x)+300, int(candidate[24].y)), (255, 0, 0), 20)
                #print(11111111111111)
                #count = count + 1
 
    	        
        elif(abs(R_heel[j-2]-R_heel[j-1]) < 2):
            #print(22222222)
            if(abs(90.0 - Angle(candidate[24].x, candidate[24].y, candidate[12].x, candidate[12].y, (candidate[24].x) - 10, candidate[24].y)) <= 80.0):
                cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[12].x), int(candidate[12].y)), (255, 0, 0), 20)
                cv2.line(image, (int(candidate[24].x), int(candidate[24].y)), (int(candidate[24].x)+300, int(candidate[24].y)), (255, 0, 0), 20)
                #count = count + 1

    return L_heel, R_heel, waist, shoulder
