import cv2

def judge2(points,spm):
    if(spm>=185):
        points=points-0
        print("spm > 185, so you will delete 0 pts")
    elif(spm>174):
        points=points-1
        print("spm < 185, so you will delete 1 pts")
    elif(spm>163):
        points=points-3
        print("spm <174, so you will delete 3 pts")
    elif(spm>151):
        points=points-6
        print("spm > 163, so you will delete 6 pts")
    else:
        points=points-9
        print("spm <151, so you will delete 9 pts")
    return points
        
