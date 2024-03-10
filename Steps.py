from Angle import Angle
import math

def Caculate_steps(candidate):
    flag, number, steps, knee_right, knee_left  = 0, 0, 0, 0, 0
    if candidate[25].visibility>=0.5 and candidate[23].visibility>=0.5 and candidate[27].visibility>=0.5:
        knee_right=Angle(candidate[25].x,candidate[25].y,candidate[23].x,candidate[23].y,candidate[27].x,candidate[27].y)
    
    if candidate[26].visibility>=0.5 and candidate[24].visibility>=0.5 and candidate[28].visibility>=0.5:
        knee_left=Angle(candidate[26].x,candidate[26].y,candidate[24].x,candidate[24].y,candidate[28].x,candidate[28].y)
    
    try:
        with open('Steps.txt', 'r') as file:
            flag = int(file.readline())
            number = int(file.readline())
            steps = int(file.readline())
        number +=1
        if knee_right > knee_left and flag == 0:
            if number > 5:
                steps += 1
                flag = 1
                number = 0
        if knee_left > knee_right and flag == 1:    
            if number > 5:
                steps += 1
                flag = 0
                number = 0

        with open('Steps.txt', 'w') as file:
            file.write(f"{flag}\n")
            file.write(f"{number}\n")
            file.write(f"{steps}\n")
        print("Total Steps: " + str(steps) + '\n')
    except FileNotFoundError:
        with open('Steps.txt', 'w') as file:
            if knee_left > knee_right:
                file.write(str(0) + '\n')
            else:
                file.write(str(1) + '\n')
            file.write(str(1) + '\n')
            file.write(str(0) + '\n')
        print("Total Steps: 0\n")
    return steps
