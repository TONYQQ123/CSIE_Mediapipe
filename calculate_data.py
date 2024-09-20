def judge_4(points, array):
    total, number = 0, 0
    array.sort()
    for i in range(1, len(array)-1):  #兩腳跟在某些時候會同時在地上  擇一刪除此時的彎腰角度
        if(array[i-1] == array[i]):
            array[i-1] = 0
    array.sort()
    for i in range(0, len(array)-1):
        if(array[i] == 0):
            number = number + 1
    array = array[number:]
    #for i in range(0, len(array)-1):
        #print(array[i])
    min = array[0]
    Max = array[len(array) - 1]
    if(min == Max):
        return (points - min)
    else:
        outcount = int(len(array)*0.05)
        finish_array = array[outcount:-outcount]
        total_len = len(finish_array)
        for i in range(0, total_len - 1):
            total = total + finish_array[i]
        points = points - (total / total_len)
        return points
