import cv2
import time
import mediapipe as mp
from Angle import Caculate_angle
import argparse
from Correct_angle import correct_angle
from Step_frequency import Calculate_step_frequency
from pathlib import Path
from step_length import s_length
from part2_judge import judge2
from shear_stress import touch1
from judge1 import judge_1
from part3 import ypos
from part3 import forearm_save
from part3_judge import judge3
from bend_over import stoop_angle
from calculate_data import judge_4
#from heel_data import heel
from draw import writepy
from Steps import touchground
from Steps import leftfoot
from Steps import rightfoot
from Correct_angle import refresh_angle
from judge1 import balance
import json
step_total_fre = 0
steps_total= 0
direction_camear = 0
bmi = float(input("please write your bmi(kg/m^2)"))
exercise_fre = int(input("one weeks how ofter day you go  jogging?(x/7)"))
forearm = int(input("please write your forearm (cm)"))
print(forearm)
def Writer(writer_buffer,detail):
    fourcc=cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, detail['fps'],(int(detail['scalar']*detail['width']), int(detail['scalar']*detail['height'])))

    for frame in writer_buffer:
        out.write(frame)   
    out.release()

        
def Photo(f_path):
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
    image=cv2.imread(f_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
            
    results = pose.process(image)
            
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    candidate=[]
            
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        temp=[landmark for landmark in results.pose_landmarks.landmark]
        for point in temp:
            point.x=point.x*(image.shape[1]-1)
            point.y=point.y*(image.shape[0]-1)
            candidate.append(point)
        image=correct_angle(candidate,image)

    scalar_factor=0.6
    image=cv2.resize(image,(0,0),fx=scalar_factor,fy=scalar_factor)        
    cv2.imshow('Pose Tracking', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def CameraorVideo(f_path,config):
    all_landmark=[]
    grade = 100
    direction = 1
    left_limit = 0
    right_limit = 0
    touchflag = 0
    step = 0
    steps = 0
    arr = []
    lower = -100
    ypositive = []
    forearm_pos = []
    scalar_factor=0.6
    writer_buffer=[]
    Landmark_Data=[]
    video_detail={}
    deduction=0
    Arr = []
    #arr1 = []
    #arr2 = []
    #arr3 = []
    #arr4 = []
    arrr = []
    #count = 0
    draw_py = []
    array = []
    lefty = []
    righty = []
    leftx = []
    rightx = []
    if f_path is not None:
        cap=cv2.VideoCapture(f_path)
    else:
        cap=cv2.VideoCapture(0)
    
    mp_pose=mp.solutions.pose
    mp_drawing=mp.solutions.drawing_utils

    start_run=time.time()

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
                
            # get video_detail
            total_frame=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            video_detail['total_frame']=total_frame
            fps=cap.get(cv2.CAP_PROP_FPS)
            video_detail['fps']=fps
            duration=total_frame/fps
            video_detail['duration']=duration
            video_detail['width']=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            video_detail['height'] = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            video_detail['scalar']=scalar_factor
	    #
            
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            
            results = pose.process(image)
            Landmark_Data.append(results)
            
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            candidate=[]
            
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                temp=[landmark for landmark in results.pose_landmarks.landmark]
            for point in temp:
                point.x=point.x*(image.shape[1]-1)
                point.y=point.y*(image.shape[0]-1)
                candidate.append(point)

            all_landmark.append(candidate)    
            temp=correct_angle(candidate,image)  
            image=temp[0]
            deduction+=temp[1]
            scalar_factor=0.3

            
            direction,left_limlt,right_limit,slength,step=s_length(candidate,direction,left_limit,right_limit,step)
            frame_index = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            fps = cap.get(cv2.CAP_PROP_FPS)
            current_time = frame_index / fps
            #------------------------------------------------
            #-----------------------
            #if(stoop_angle(candidate, Arr) != -1):
                #Arr = stoop_angle(candidate, Arr)
            direction_camear = refresh_angle(candidate) 
              
            Arr, flag = stoop_angle(candidate, Arr, image)
            
            ypositive = ypos(candidate,ypositive)
            lefty = leftfoot(candidate,lefty)
            righty,lower,leftx,rightx = rightfoot(candidate,righty,image,lower,leftx,rightx,direction_camear)
            step_total_fre,touchflag =Calculate_step_frequency(candidate,current_time,array,steps,touchflag,image)
            arr = touch1(candidate,arr,image)
            
            
            forearm_pos = forearm_save(candidate,forearm_pos,direction_camear)
            draw_py = writepy(candidate,draw_py)
            #degrees = touchground(candidate, array, steps,degrees)##################
            #ans = show_leg(candidate)
            #step_total=total_step(candidate,current_time)
            #print(step_total_fre)
            #------------------------------------------------
            #print(current_time)
            
            image=cv2.resize(image,(0,0),fx=scalar_factor,fy=scalar_factor)   
            writer_buffer.append(image)     
            cv2.imshow('Pose Tracking', image)     
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    end_run=time.time()
    run_duration=(end_run-start_run)
    points=int(run_duration)*config['reward']-deduction
    write_start_time=time.time()
    if f_path is not None:   
        Writer(writer_buffer,video_detail)
    write_end_time=time.time()
    print('------------Video Details----------------')
    #print(type(step_total_fre))
    fre = round (step_total_fre)
    #print(type(fre))
    print("total_step_fre ",fre)
    print("initial your grade is = ",grade)
    #point = judge2(point,fre)
    arr,grade = judge_1(grade,arr)
    print("After in part 1 , your grade = ",grade)
    grade = judge2(grade,fre)
    print("After in part 2 , your grade = ",grade)
    #print(arr)
    #print(arr)
    print(type(fre))
    grade = judge3(grade,ypositive,forearm_pos,forearm)
    print("After in part 3 , your grade = ",grade)
    grade = judge_4(grade, Arr)
    print("After in part 4 , your grade = ",grade)
    
    #arrr = stoop_angle(arrr, arr1, arr2, arr3, arr4)
    #grade = judge_4(grade, arrr)
    grade = balance(grade,bmi,exercise_fre)
    print("after balace your grade =",grade)
    #print("count = ", count)
    print(f'fps: {video_detail["fps"]}\norigin video length: {video_detail["duration"]}\ntotal_frame: {video_detail["total_frame"]}')
    #print(all_landmark)
    cap.release()
    cv2.destroyAllWindows()
    

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--mode',choices=['photo','video','camera'])
    parser.add_argument('--file')
    arg=parser.parse_args()

    with open('config.json') as f:
        config=json.load(f)
    #start_time = time.perf_counter()\
    s_time = time.time()
  
    if arg.mode=='photo':
        Photo(arg.file)

    if arg.mode=='video':
        CameraorVideo(arg.file,config)

    
    if arg.mode=='camera':
        CameraorVideo(None,config)
    e_time = time.time()
    #total_step = #max_step
    print(f'Total time: {e_time-s_time}')
    #print(total_step)
    print('-------------------------------------')




if __name__=='__main__':
    main()


