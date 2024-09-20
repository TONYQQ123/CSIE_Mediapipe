from Angle import Angle
import math

def ypos(candidate,array):
    #trp = candidate[23].x + candidate[24].x
    zrp = candidate[23].y + candidate[24].y
    array.append(zrp)
    with open('part3.txt','a') as file:
        file.write(str(zrp)+'\n')
    return array
def forearm_save(candidate,array,direction):
    if (direction == 1): # 16 14 判斷左鏡頭視角跟又鏡頭視角，取出比例尺，這邊以手臂判斷
    	pos = math.sqrt(((candidate[14].x - candidate[16].x)*(candidate[14].x - candidate[16].x)) + ((candidate[14].y - candidate[16].y)*(candidate[14].y - candidate[16].y)))
    	array.append(pos)
    else:
        pos = math.sqrt((candidate[13].x - candidate[15].x)*(candidate[13].x - candidate[15].x) + (candidate[13].y - candidate[15].y)*(candidate[13].y - candidate[15].y))
        array.append(pos)
    return  array
