import cv2
import mediapipe as mp
from Angle import Caculate_angle
import argparse
from Correct_angle import correct_angle
import time
from Step_frequency import Calculate_step_frequency
from pathlib import Path
from step_length import s_length
from step_length import s_length
import time
import json
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
    direction = 1
    left_limit = 0
    right_limit = 0
    
    scalar_factor=0.6
    writer_buffer=[]
    Landmark_Data=[]
    video_detail={}
    deduction=0
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
            temp=correct_angle(candidate,image)  
            image=temp[0]
            deduction+=temp[1]
            scalar_factor=0.3

            direction,left_limlt,right_limit,slength=s_length(candidate,direction,left_limit,right_limit)
            frame_index = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            fps = cap.get(cv2.CAP_PROP_FPS)
            current_time = frame_index / fps
            #------------------------------------------------
            Calculate_step_frequency(candidate,current_time)
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
    print(f'fps: {video_detail["fps"]}\norigin video length: {video_detail["duration"]}\ntotal_frame: {video_detail["total_frame"]}')
    cap.release()
    cv2.destroyAllWindows()
    

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--mode',choices=['photo','video','camera'])
    parser.add_argument('--file')
    arg=parser.parse_args()

    with open('config.json') as f:
        config=json.load(f)
    
    start_time = cv2.getTickCount()
    s_time = time.time()
  
    if arg.mode=='photo':
        Photo(arg.file)

    if arg.mode=='video':
        CameraorVideo(arg.file,config)
        file = Path('Steps.txt')
        file.unlink()

    
    if arg.mode=='camera':
        CameraorVideo(None,config)
    end_time = cv2.getTickCount()
    e_time = time.time()
    during_time = (end_time-start_time)/cv2.getTickFrequency()
    print(during_time)
    print(f'Total time: {e_time-s_time}')
    print('-------------------------------------')




if __name__=='__main__':
    main()


