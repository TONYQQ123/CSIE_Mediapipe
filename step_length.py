import numpy as np
import cv2
import math
#candidate is x and y coodriate
#direction is diction1
#left_limit is lelim
#right_limit is rilim
def s_length(candidate,diction1,lelim,rilim):
	if lelim is None:
	    lelim = 0
	    direction = 1
	    rilim = 1
	m = candidate[28].x #right foot x coodit
	n = candidate[28].y #right foot y coodit
	direction=diction1
	tall = math.sqrt((candidate[28].x-candidate[26].x)*(candidate[28].x-candidate[26].x)+(candidate[28].y-candidate[26].y)*(candidate[26].y-candidate[26].y))
	tall = 0
	tall = tall + math.sqrt((candidate[26].x-candidate[24].x)*(candidate[26].x-candidate[24].x)+(candidate[26].y-candidate[24].y)*(candidate[26].y-candidate[24].y))
	
	tall = tall + math.sqrt((candidate[24].x-candidate[12].x)*(candidate[24].x-candidate[12].x)+(candidate[24].y-candidate[12].y)*(candidate[24].y-candidate[12].y))
	
	tall = tall + math.sqrt((candidate[12].x-candidate[0].x)*(candidate[12].x-candidate[0].x)+(candidate[12].y-candidate[0].y)*(candidate[12].y-candidate[0].y))
	real_tall = 170  # is the user tall (cm)
	px = real_tall / tall 
	px = px / 1.5
	px = px / 1.33
	#print("------------------")
	#m, n = map(int, input().split())#suppose we use right foot
	# m is the x coodriate so is coo[13][0]
	# n is the y coodriate so is coo[13][1]
	stride_length = 0
	#---------------------------------------
	left_limit_x= lelim
	right_limit_x= rilim
	#left_limit_x, right_limit_x = m, m
	#left_limit_y, right_limit_y = n, n
	#direction = 1  # turn right is 1, turn left is -1
	with open('stride_length.txt','a') as file:
	    file.write('the program sta222rt'+'\n')
	print(m, n)
	#while m != 0 and n != 0:
	    #m, n = map(int, input().split())
	if direction == 1:
		if m < right_limit_x:
			direction = -1
			stride_length = right_limit_x - left_limit_x
			stride_length_r = stride_length * px
			with open('stride_length.txt','a') as file:
			    file.write('the stride_length is '+str(stride_length_r)+'\n')
			print("此次步輻為PX", stride_length_r)
			# candidate[10][0]= left foot x coodit
			print("TWO FOOT DISTANCE",math.sqrt((candidate[28].x-candidate[27].x)*(candidate[28].x-candidate[27].x)+(candidate[28].y-candidate[27].y)*(candidate[28].y-candidate[27].y))/px)
			stride_length = 0
			left_limit_x = m
		else:
			right_limit_x = m
	else:  # turn left
		if m > left_limit_x:
			direction = 1
			stride_length = right_limit_x - left_limit_x
			stride_length_r = stride_length * px
			with open('stride_length.txt','a') as file:
			    file.write('the stride_length is '+str(stride_length_r)+'\n')
			print("此次步輻為PX", stride_length_r)
			print("TWO FOOT DISTANCE",math.sqrt((candidate[28].x-candidate[27].x)*(candidate[28].x-candidate[27].x)+(candidate[28].y-candidate[27].y)*(candidate[28].y-candidate[27].y))/px)
			stride_length = 0
			right_limit_x = m
		else:
			left_limit_x = m
			with open('stride_length.txt','a') as file:
			    file.write('m = '+str(m)+' n = '+str(n)+' left_limit_x = '+str(left_limit_x)+' right_limit= '+str(right_limit_x)+' direction = '+str(direction)+'\n')
			
		print("m =", m, "n =", n, "left_limit =", left_limit_x, "right_limit =", right_limit_x, "direction =", direction)
	return(direction,left_limit_x,right_limit_x,stride_length)
	
def stride_length(candidate,diction1,lelim,rilim):
    data=s_length(candidate,diction1,lelim,rilim)
    return data[3]
    
	

