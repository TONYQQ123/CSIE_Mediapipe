import cv2
import math
def judge_1(grade,array):
    sort_array=sorted(array)
    outcount = int(len(sort_array) * 0.05)
    finish_array = sort_array[outcount:-outcount]
    total_len=len(finish_array)
    point = 0
    for x in range(0,total_len-1):
        if (finish_array[x]<80):
            point = point + ((80-finish_array[x])/total_len)
    grade = grade - point
    return finish_array,grade
def balance(grade,bmi,exercise_fre):
    sub = 100 - grade
    level = 0
    if (exercise_fre>=5):
        if(bmi>27):
            level = 3
        elif(bmi>24):
            level = 4
        else:
            level = 5
    elif(exercise_fre>=3):
        if(bmi>27):
            level = 2
        elif(bmi>24):
            level = 3
        else:
            level = 4
    elif(exercise_fre>=1):
        if(bmi>27):
            level = 1
        elif(bmi>24):
            level = 2
        elif(bmi >=18.5):
            level = 3
        else:
            level = 2
    else:
        if(18.5<=bmi<=24):
            level = 2
        else:
            level = 1
    sub = ((level) * 0.2) * sub
    grade = 100 - sub
    return grade
