from Angle import Angle
import cv2
import json
def y_position(candidate, array):
    center = candidate[24].y + candidate[23].y
    array.append(center)
    #with open('y_position.txt','a') as file:
    #    file.write(str(center)+'\n')  
    return array
def leftfoot(candidate, array):
    left = candidate[29].y
    array.append(left)
    #print(left)
    return array
def rightfoot(candidate, array,image,lower,leftx,rightx,diction):
    right = candidate[30].y
    leftpos = candidate[30].x
    rightpos = candidate[29].x
    array.append(right)
    leftx.append(leftpos)
    rightx.append(rightpos)
    flag = 0
    dic = diction
    #print(len(array)-1) # now pos
    if (len(array)>2):
        #print(len(array))
        pos = len(array)-1
        posx = len(leftx)-1
        if (array[pos]< array[pos-1] and array[pos-2]<array[pos-1]):
            if (lower < array[pos-1]):
                lower = array[pos-1]
                flag = 1
            elif(lower * 0.9 < array[pos-1]):
                flag = 1
            elif lower == -100:
                flag = 0
            #print(pos-1) # small point
            if flag == 1:
                #print("low_point",array[pos-1])
                #print("low_pointx",leftx[posx-1])
                #print(candidate[30].x)
                #print(leftpos[pos-1])
                c2324x = (candidate[23].x+candidate[24].x)/2
                c2324y = (candidate[23].y+candidate[24].y)/2
                if(dic == 0):
                    degree = Angle(leftx[posx-1],array[pos-1],c2324x,c2324y,leftx[posx-1]+10,array[pos-1])
                else:
                    degree = Angle(leftx[posx-1],array[pos-1],c2324x,c2324y,leftx[posx-1]-10,array[pos-1])
                #print("Degree = ",degree)
                perfectA = (255,0,255)  
                goodB = (0,0,255)
                wellC =(0,255,0)
                okD = (255,255,0)
                badE =(255,0,0)
                if(80<=degree<=90):
                    color = perfectA
                elif(degree>90 or degree< 80):
                    if(degree>90):
                        sub = degree-90
                    else:
                        sub = 80-degree
                    if(sub<1.5):
                        color = goodB
                    elif(sub<3.5):
                        color = wellC
                    elif(sub<6.5):
                        color = okD
                    else:
                        color = badE
                if (dic == 0):
                    cv2.line(image, (int(leftx[posx-1]), int(array[pos-1])), (int(leftx[posx-1]) + 300, int(array[pos-1])),color, 15)
                else:
                    cv2.line(image, (int(leftx[posx-1]), int(array[pos-1])), (int(leftx[posx-1]) - 300, int(array[pos-1])),color, 15)
                cv2.line(image, (int(c2324x), int(c2324y)), (int(leftx[posx-1]), int(array[pos-1])), color, 15)
    #print(right)
    return array,lower,leftx,rightx
def Calculate_steps(candidate, array, steps,flags,image):
    array = y_position(candidate, array)
    flags = 0
    #with open('y_position.txt', 'r') as file:
    #    lines = file.readlines()

    #y = [float(line.strip()) for line in lines]

    #for i in range(1, len(y) - 1):
    #    if y[i-1] > y[i] and y[i] < y[i+1]:
    #        steps += 1
    step = steps
    for i in range(1, len(array) - 1):
        if array[i-1] > array[i] and array[i] < array[i+1]:
            steps += 1
            flags = 1
        else:
            flags = 0
    if step != steps:
        array = []
    if flags == 1:
        heavypointy = candidate[24].y + candidate[23].y
        heavypointx = candidate[24].y + candidate[23].y
        if(candidate[29].y<candidate[30].y):# left
            #print("AAAAAAAAAAAAAAAAAA")
            degree = Angle(candidate[29].x,candidate[29].y,heavypointx,heavypointy,candidate[29].x + 20 , candidate[29].y)
            #cv2.line(image, (int(candidate[23].x), int(candidate[23].y)), (int(candidate[29].x), int(candidate[29].y)), (0,0,0), 15)
            #cv2.line(image, (int(candidate[23].x), int(candidate[23].y)), (int(candidate[24].x), int(candidate[24].y)), (0,0,0), 15)
            #cv2.line(image, (int(candidate[29].x), int(candidate[29].y)), (int(candidate[29].x) + 300, int(candidate[29].y)), (0,0,0), 15)
                #degrees.append(degree)
            #rint("degree = ",degree)
        else:
            #print("BBBBBBBBBBBBBBBB")
            degree = Angle(candidate[30].x,candidate[30].y,heavypointx,heavypointy,candidate[30].x + 20 , candidate[30].y)
            #cv2.line(image, (int(candidate[23].x), int(candidate[23].y)), (int(candidate[30].x), int(candidate[30].y)), (255,255,255), 15)
            #cv2.line(image, (int(candidate[23].x), int(candidate[23].y)), (int(candidate[24].x), int(candidate[24].y)), (0,0,0), 15)
            #cv2.line(image, (int(candidate[30].x), int(candidate[30].y)), (int(candidate[30].x) + 300, int(candidate[30].y)), (0,0,0), 15)
            #print("degree = ",degree)
    #print("Steps: " + str(steps) + '\n')
    #print("fkags = ",flags)
    return steps,flags
def touchground(candidate, array, steps,degrees):
    array = y_position(candidate,array)
    for i in range(1, len(array) - 1):
        if array[i-1] > array[i] and array[i] < array[i+1]:
            #calculate the degree
            heavypointy = candidate[24].y + candidate[23].y
            heavypointx = candidate[24].y + candidate[23].y
            if(candidate[29].y<candidate[30].y):# left
                degree = Angle(candidate[29].x,candidate[29].y,heavypointx,heavypointy,candidate[29].x + 20 , candidate[29].y)
                degrees.append(degree)
                print("degree = ",degree)
            else:
                degree = Angle(candidate[30].x,candidate[30].y,heavypointx,heavypointy,candidate[30].x + 20 , candidate[30].y)
                print("degree = ",degree)
                degrees.append(degree)
    return degrees