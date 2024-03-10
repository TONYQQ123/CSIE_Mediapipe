import cv2
import mediapipe as mp
from Angle import Caculate_angle
import argparse
from Correct_angle import correct_angle
import time
from Step_frequency import Calculate_step_frequency
from pathlib import Path


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


def CameraorVideo(f_path):
    if f_path is not None:
        cap=cv2.VideoCapture(f_path)
    else:
        cap=cv2.VideoCapture(0)
    mp_pose=mp.solutions.pose
    mp_drawing=mp.solutions.drawing_utils

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
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
            scalar_factor=0.3

            image=correct_angle(candidate,image)
            
            frame_index = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            fps = cap.get(cv2.CAP_PROP_FPS)
            current_time = frame_index / fps
            Calculate_step_frequency(candidate,current_time)
            #print(current_time)
            
            scalar_factor=0.6
            image=cv2.resize(image,(0,0),fx=scalar_factor,fy=scalar_factor)        
            cv2.imshow('Pose Tracking', image)     
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()
    



if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--mode',choices=['photo','video','camera'])
    parser.add_argument('--file')
    arg=parser.parse_args()
    
    start_time = cv2.getTickCount()
    
    if arg.mode=='photo':
        Photo(arg.file)

    if arg.mode=='video':
        CameraorVideo(arg.file)

        file = Path('Steps.txt')
        file.unlink()

    
    if arg.mode=='camera':
        CameraorVideo(None)
    #end_time = cv2.getTickCount()
    #during_time = (end_time-start_time)/cv2.getTickFrequency()
    #print(during_time)


