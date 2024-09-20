import cv2
import math
import numpy as np
def judge3(grade,array,scale,real_forearm):
    #array has zrp all y information
    percent_scale5 = np.percentile(scale, 5)
    percent_scale95 = np.percentile(scale, 95)
    filtered_scale = [x for x in scale if percent_scale5 <= x <= percent_scale95]
    average_scale = np.mean(filtered_scale)
    print("scale = ",average_scale)
    pixel = real_forearm / average_scale
    y_values = array
    high_points = []
    low_points = []
    for i in range(1, len(y_values) - 1):
    # 计算当前点和前一个点的斜率
        slope_before = y_values[i] - y_values[i - 1]
    # 计算当前点和后一个点的斜率
        slope_after = y_values[i + 1] - y_values[i]

    # 斜率变化点
        if slope_before > 0 and slope_after < 0:
        # 相对高点
            high_points.append((i, y_values[i]))
        elif slope_before < 0 and slope_after > 0:
        # 相对低点
            low_points.append((i, y_values[i]))
    # x 轴坐标值从 1 开始，间隔为 627.88525390625
    x_values = [i * 627.88525390625 for i in range(1, len(y_values) + 1)]


    #-----------處理最高點部分
    x_values_high = [point[0] for point in high_points]
    y_values_high = [point[1] for point in high_points]
    percentile_5 = np.percentile(y_values_high, 5)
    percentile_95 = np.percentile(y_values_high, 95)

    filtered_high_points = [(x, y) for x, y in high_points if percentile_5 <= y <= percentile_95]

    x_values_high = [point[0] for point in filtered_high_points]
    y_values_high = [point[1] for point in filtered_high_points]
    average_y_high = np.mean(y_values_high)
    #plt.plot(x_values_high,y_values_high, marker='o', linestyle='-')
    #------處理完畢
    #------處理低點部分
    x_values_low = [point[0] for point in low_points]
    y_values_low = [point[1] for point in low_points]
    percentile_5_l = np.percentile(y_values_low, 5)
    percentile_95_l = np.percentile(y_values_low, 95)

    filtered_low_points = [(x, y) for x, y in low_points if percentile_5_l <= y <= percentile_95_l]

    x_values_low = [point[0] for point in filtered_low_points]
    y_values_low = [point[1] for point in filtered_low_points]
    average_y_low = np.mean(y_values_low)
    #print("average high = ",average_y_high)
    #print("average low = ",average_y_low)
    amplitude = (average_y_high-average_y_low)/2 # void positive
    print("amplitude = ",amplitude)
    real_amplitude = pixel * amplitude
    print("real_amplitude = ",real_amplitude)
    if(real_amplitude<6.4):
        grade=grade-0
        print("amplitude < 6.4 , delete 0 pts")
    elif(real_amplitude<=8.1):
        grade=grade-1
        print("amplitude < 8.1 , delete 1 pts")
    elif(real_amplitude<=9.7):
        grade=grade-3
        print("amplitude < 9.7 , delete 3 pts")
    elif(real_amplitude<=11.5):
        grade=grade-6
        print("amplitude < 11.5 , delete 6 pts")
    else:
        grade=grade-9
        print("amplitude >>> 11.5 , delete 9 pts")
    return grade
    
