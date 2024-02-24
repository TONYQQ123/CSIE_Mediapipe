import cv2
import mediapipe as mp
from Angle import Caculate_angle
import argparse

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
        candidate=[landmark for landmark in results.pose_landmarks.landmark]
        Caculate_angle(candidate)

    scalar_factor=0.3
    image=cv2.resize(image,(0,0),fx=scalar_factor,fy=scalar_factor)        
    cv2.imshow('Pose Tracking', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def Camera():
    cap = cv2.VideoCapture(0)
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
                candidate=[landmark for landmark in results.pose_landmarks.landmark]
                Caculate_angle(candidate)          
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

    if arg.mode=='photo':
        Photo(arg.file)

    if arg.mode=='video':
        print('Coming soon!')
    
    if arg.mode=='camera':
        Camera()



