from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog, QGraphicsScene
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QImage, QPixmap
import numpy as np

import cv2
import time
import mediapipe as mp
from Correct_angle import correct_angle
from Step_frequency import Calculate_step_frequency
from part2_judge import judge2
from shear_stress import touch1
from judge1 import judge_1
from part3 import ypos
from part3 import forearm_save
from part3_judge import judge3
from bend_over import stoop_angle
from calculate_data import judge_4
from judge_all import judge_action
from Steps import leftfoot
from Steps import rightfoot
from Correct_angle import refresh_angle
from judge1 import balance
import json

from ui.lib.share import Share_Info as SI
import requests
from datetime import datetime
from Data_api.account_api import accountAPI as api

step_total_fre = 0
steps_total= 0
def Writer(writer_buffer,detail):
    fourcc=cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, detail['fps'],(int(detail['scalar']*detail['width']), int(detail['scalar']*detail['height'])))

    for frame in writer_buffer:
        out.write(frame)   
    out.release()

class Window_Sign_in:

    def __init__(self):
        self.ui = QUiLoader().load('ui/Sign_in.ui')
        self.ui.log_in.clicked.connect(self.Log_in)
        self.ui.sign_up.clicked.connect(self.Sign_up)
        self.ui.password.returnPressed.connect(self.Log_in)


    def Log_in(self):
        username = self.ui.username.text().strip()
        password = self.ui.password.text().strip()
        
        response = account.login(username,password)
        if response.status_code!=200:
            QMessageBox.warning(
                self.ui,
                'Error',
                response.json().get('error'))
            return
        #else:
        #    QMessageBox.information(
        #        self.ui,
        #        'Successful',
        #        response.json().get('message'))
        SI.Home_Window = Window_Home()
        SI.Home_Window.ui.show()
        self.ui.password.setText('')
        self.ui.hide()
    
    def Sign_up(self):
        SI.Sign_up_Window = Window_Sign_up()
        SI.Sign_up_Window.ui.show()
        self.ui.close()

class Window_Home :

    def __init__(self):
        self.ui = QUiLoader().load('ui/Home.ui')
        self.ui.information.clicked.connect(self.Information)
        self.ui.rank.clicked.connect(self.Rank)
        self.ui.run_detect.clicked.connect(self.Run_detect)
        self.ui.activity.clicked.connect(self.Activity)
    
    def Information(self):
        SI.Information_Window = Window_Information()
        SI.Information_Window.ui.show()
        self.ui.close()

    def Rank(self):
        SI.Rank_Window = Window_Rank()
        SI.Rank_Window.ui.show()
        self.ui.close()

    def Run_detect(self):
        SI.Run_detect_Window = Window_Run_detect()
        SI.Run_detect_Window.ui.show()
        self.ui.close()
    
    def Activity(self):
        SI.Activity_Window = Window_Activity()
        SI.Activity_Window.ui.show()
        self.ui.close()
    
class Window_Sign_up :

    def __init__(self):
        self.ui = QUiLoader().load('ui/Sign_up.ui')
        self.ui.back.clicked.connect(self.Back)
        self.ui.Register.clicked.connect(self.Register)

    def Back(self):
        SI.Login_Window.ui.show()
        self.ui.close()

    def Register(self):
        username = self.ui.username.text().strip()
        password = self.ui.password.text().strip()
        #born = self.ui.born.text().strip()
        #height = self.ui.Height.text().strip()
        #weight = self.ui.weight.text().strip()

        response = account.register(username,password)

        if response.status_code!=201:
            QMessageBox.warning(
                self.ui,
                'Error',
                response.json().get('error'))
            return
        else:
            QMessageBox.information(
                self.ui,
                'Successful',
                response.json().get('message'))

        SI.Login_Window = Window_Sign_in()
        SI.Login_Window.ui.show()
        self.ui.close()

class Window_Information :

    def __init__(self):
        self.ui = QUiLoader().load('ui/Information.ui')
        self.ui.back.clicked.connect(self.Back)
        self.ui.Update.clicked.connect(self.Update)
        self.ui.log_out.clicked.connect(self.Log_out)
        response = account.get_account_detail()
        if response.status_code==400:
            QMessageBox.warning(
                self.ui,
                'Error',
                response.json().get('error'))
            return
        elif response.status_code==200:
            self.ui.username.setText(response.json().get('username'))
            born = datetime.strptime(response.json().get('born'), "%Y-%m-%dT%H:%M:%SZ")
            self.ui.born.setText(born.strftime("%Y/%m/%d"))
            self.ui.Height.setText(str(response.json().get('height')))
            self.ui.weight.setText(str(response.json().get('weight')))
            self.ui.score.setText(str(response.json().get('score')))
            self.ui.spend_time.setText(str(response.json().get('spend_time')))

    def Back(self):
        SI.Home_Window.ui.show()
        self.ui.close()

    def Update(self):
        SI.Update_Information_Window = Window_Update_Information()
        SI.Update_Information_Window.ui.show()
        self.ui.close()
    
    def Log_out(self):
        self.url = url+'logout/'
        response=requests.Session().get(self.url)
        if response.status_code==200:
            QMessageBox.information(
                self.ui,
                'Successful',
                response.json().get('message'))
        else:
            QMessageBox.warning(
                self.ui,
                'Error',
                response.json().get('error'))
            return
        SI.Login_Window.ui.show()
        self.ui.close()
        
class Window_Update_Information :
    
    def __init__(self):
        self.ui = QUiLoader().load('ui/Update_Information.ui')
        self.ui.back.clicked.connect(self.Back)
        self.ui.save.clicked.connect(self.Save)

    def Back(self):
        SI.Information_Window.ui.show()
        self.ui.close()

    def Save(self):
        born = datetime.strptime(self.ui.born.text().strip(), "%Y/%m/%d")
        height = self.ui.Height.text().strip()
        weight = self.ui.weight.text().strip()
        
        idata = {
            "height" : height,
            "weight" : weight,
            "born" : born.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        response = account.update_information(idata)

        if response.status_code!=200:
            QMessageBox.warning(
                self.ui,
                'Error',
                response.json().get('error'))
            return
        else:
            QMessageBox.information(
                self.ui,
                'Successful',
                response.json().get('message'))
        SI.Information_Window = Window_Information()
        SI.Information_Window.ui.show()
        self.ui.close()

class Window_Rank :

    def __init__(self):
        self.ui = QUiLoader().load('ui/Rank.ui')
        self.ui.back.clicked.connect(self.Back)

        response = account.rank()
        if response.status_code!=200:
            QMessageBox.warning(
                self.ui,
                'Error',
                response.json().get('error'))
            return
        else:
            self.ui.current_rank.setText(str(response.json().get('current_rank')))
            response_json = response.json()
            for i in range(1, 11):
                if i <= len(response_json['top_10']):
                    user = response_json['top_10'][i-1]
                    getattr(self.ui, f'rank{i}_name').setText(str(user['username']))
                    getattr(self.ui, f'rank{i}_score').setText(str(user['score']))
                else:
                    getattr(self.ui, f'rank{i}_name').setText('')
                    getattr(self.ui, f'rank{i}_score').setText('')

    def Back(self):
        SI.Home_Window.ui.show()
        self.ui.close()

class Window_Run_detect:
    def __init__(self):
        self.ui = QUiLoader().load('ui/Run_detect.ui')
        self.ui.back.clicked.connect(self.Back)
        self.ui.start.clicked.connect(self.Start)
        self.ui.stop.clicked.connect(self.Stop)
        self.ui.search.clicked.connect(self.search)
        self.ui.photo.clicked.connect(lambda: self.set_mode('photo'))
        self.ui.camera.clicked.connect(lambda: self.set_mode('camera'))
        self.ui.video.clicked.connect(lambda: self.set_mode('video'))

        self.mode = None
        self.direction_camear = None
        self.image = None
        self.stop = False

    def set_mode(self, mode):
        self.mode = mode

    def Back(self):
        SI.Home_Window.ui.show()
        self.ui.close()

    def Stop(self):
        self.stop = True

    def Start(self):
        if self.mode == 'photo' and self.ui.filepath.text() != '':
            
            mp_pose = mp.solutions.pose
            mp_drawing = mp.solutions.drawing_utils
            pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
            image=cv2.imread(self.ui.filepath.text())
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

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, channel = image.shape
            bytesPerLine = 3 * width
            qimage = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimage)
            if (pixmap.height() / pixmap.width()) > (9 / 16):
                scaled_pixmap = pixmap.scaledToHeight(self.ui.output.height()-5)
            else:
                scaled_pixmap = pixmap.scaledToWidth(self.ui.output.width()-5)
            scene = QGraphicsScene()
            scene.addPixmap(scaled_pixmap)
            self.ui.output.setScene(scene)

        elif self.mode == 'camera' or (self.mode == 'video' and self.ui.filepath.text() != ''):
            forearm_length =  float(self.ui.forearm_length.text().strip())
            exercise_fre = int(self.ui.exercise_fre.text().strip())
            self.ui.score.setText('')
            if forearm_length == '':
                QMessageBox.warning(
                    self.ui,
                    'Error',
                    'Please input forearm length')
                return
            
            if exercise_fre == '':
                QMessageBox.warning(
                    self.ui,
                    'Error',
                    'Please input exercise frequency')
                return

            response = account.get_account_detail()
            if response.status_code==400:
                QMessageBox.warning(
                    self.ui,
                    'Error',
                    response.json().get('error'))
                return
            elif response.status_code==200:
                wt = response.json().get('weight')
                ht = response.json().get('height')

            bmi = wt / ((ht/100)**2)

            with open('config.json') as f:
                config=json.load(f)
            arr_time, step_total_fre_time, forearm_pos_time = 0, 0, 0
            all_landmark=[]
            grade = 100
            touchflag = 0
            steps = 0
            arr = []
            ypositive = []
            forearm_pos = []
            scalar_factor=0.6
            writer_buffer=[]
            Landmark_Data=[]
            video_detail={}
            deduction=0
            current_time=0
            Arr = []
            array = []

            lefty = []
            righty = []
            leftx = []
            rightx = []
            lower = -100
            if self.ui.filepath.text() is not None:
                cap=cv2.VideoCapture(self.ui.filepath.text())
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
                    
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    image.flags.writeable = False
                    
                    results = pose.process(image)
                    Landmark_Data.append(results)
                    
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                    candidate=[]
                    landmark_data = []
                    txt = ''
                    if results.pose_landmarks:
                        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                        temp=[landmark for landmark in results.pose_landmarks.landmark]
                    for point in temp:
                        point.x=point.x*(image.shape[1]-1)
                        point.y=point.y*(image.shape[0]-1)
                        candidate.append(point)
                        landmark_data.append({'x':round(point.x,2),'y':round(point.y,2),'visibility':round(point.visibility,2)})
                    all_landmark.append(landmark_data)
                    temp=correct_angle(candidate,image)  
                    image=temp[0]
                    deduction+=temp[1]
                    scalar_factor=0.3
                    frame_index = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
                    fps = cap.get(cv2.CAP_PROP_FPS)
                    current_time = frame_index / fps
                    direction_camera = refresh_angle(candidate)
                    
                    Arr, flag = stoop_angle(candidate, Arr, image)
                    
                    ypositive = ypos(candidate,ypositive)
                    
                    lefty = leftfoot(candidate,lefty)
                    righty,lower,leftx,rightx = rightfoot(candidate,righty,image,lower,leftx,rightx,direction_camera)

                    step_total_fre,touchflag= Calculate_step_frequency(candidate,current_time,array,steps,touchflag,image)
                    arr = touch1(candidate,arr,image)
                    
                    
                    forearm_pos = forearm_save(candidate,forearm_pos,direction_camera)
                    
                    txt = judge_action(arr, step_total_fre, forearm_pos, arr_time, step_total_fre_time, forearm_pos_time, fps, flag)
                    
                    height, width, channel = image.shape
                    bytesPerLine = 3 * width
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    qimage = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(qimage)
                    if (pixmap.height() / pixmap.width()) > (9 / 16):
                        scaled_pixmap = pixmap.scaledToHeight(self.ui.output.height()-5)
                    else:
                        scaled_pixmap = pixmap.scaledToWidth(self.ui.output.width()-5)
                    scene = QGraphicsScene()
                    scene.addPixmap(scaled_pixmap)
                    self.ui.output.setScene(scene)
                    QApplication.processEvents()  # 強制處理事件隊列中的事件

                    self.ui.spend_time.setText(str(round(current_time)))
                    self.ui.step_frequency.setText(str(round(step_total_fre / 5) * 5))
                    self.ui.suggestion.setText(str(txt))
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    if self.stop:
                        break

            video_detail['forearm_length'] = forearm_length
            video_detail['exercise_fre'] = exercise_fre
            video_detail['bmi'] = bmi
            
            end_run=time.time()
            run_duration=(end_run-start_run)
            points=int(run_duration)*config['reward']-deduction
            write_start_time=time.time()
            if self.ui.filepath.text() is not None:   
                Writer(writer_buffer,video_detail)
            write_end_time=time.time()

            print('------------Video Details----------------')
            print('Steps', steps)
            fre = round (step_total_fre)
            print("total_step_fre ",fre)
            print("initial your grade is = ",grade)
            arr,grade = judge_1(grade,arr)
            print("After in part 1 , your grade = ",grade)
            grade = judge2(grade,fre)
            print("After in part 2 , your grade = ",grade)
            print(type(fre))
            grade = judge3(grade,ypositive,forearm_pos,forearm_length)
            print("After in part 3 , your grade = ",grade)
            
            grade = judge_4(grade, Arr)
            print("After in part 4 , your grade = ",grade)
            #balance function 
            grade = balance(grade,bmi,exercise_fre)
            print(f'fps: {video_detail["fps"]}\norigin video length: {video_detail["duration"]}\ntotal_frame: {video_detail["total_frame"]}')

            self.ui.score.setText(str(round(grade,1)))
            account.update_video_detail(video_detail)
            account.update_all_landmark(all_landmark)
            account.update_spend_time(round(current_time))
            account.update_score(grade)
            cap.release()
            
        else:
            QMessageBox.warning(
                self.ui,
                'Error',
                'Please select mode or filepath')
            return

        self.stop = False


    def search(self):
        if self.mode == 'photo':
            file_filter = "Image Files (*.jpg *.png *.bmp)"
        elif self.mode == 'video':
            file_filter = "Video Files (*.mp4 *.avi)"
        else:
            file_filter = "All Files (*.*);;Image Files (*.jpg *.png *.bmp);;Video Files (*.mp4 *.avi)"

        file_path, _ = QFileDialog.getOpenFileName(self.ui, "Select File", "", file_filter)
        if file_path:
            self.ui.filepath.setText(file_path)

class Keypoint:
    def __init__(self, x, y, visibility):
        self.x = x
        self.y = y
        self.visibility = visibility
class Window_Activity :
    
    def __init__(self):
        self.ui = QUiLoader().load('ui/Activity.ui')
        self.ui.back.clicked.connect(self.Back)
        self.ui.start.clicked.connect(self.Start)
        self.ui.stop.clicked.connect(self.Stop)
        self.image = None
        self.stop = False
    
    def Back(self):
        SI.Home_Window.ui.show()
        self.ui.close()

    def Start(self):
        response = account.get_account_detail()
        if response.status_code==400:
            QMessageBox.warning(
                self.ui,
                'Error',
                response.json().get('error'))
            return
        elif response.status_code==200:
            all_landmark_dict = response.json().get('all_landmarks')
        if all_landmark_dict== []:
            QMessageBox.warning(
                self.ui,
                'Error',
                'No data')
            return
        else:
            self.ui.score.setText('')
            arr_time, step_total_fre_time, forearm_pos_time = 0, 0, 0
            grade = 100
            touchflag = 0
            steps = 0
            arr = []
            ypositive = []
            forearm_pos = []
            video_detail={}
            Arr = []
            array = []

            lefty = []
            righty = []
            leftx = []
            rightx = []
            lower = -100
            
            frame_index = 0
            video_detail = response.json().get('video_detail')
            fps = video_detail['fps']
            width = video_detail['width']
            height = video_detail['height']
            forearm_length = video_detail['forearm_length']
            exercise_fre = video_detail['exercise_fre']
            bmi = video_detail['bmi']
            start_time = cv2.getTickCount()

            for landmark in all_landmark_dict:
                candidate = []
                points = [Keypoint(pt['x'], pt['y'], pt['visibility']) for pt in landmark]
                candidate.extend(points)
                image = np.ones((height, width, 3), dtype=np.uint8)
                for point in landmark:
                    x, y, visibility = point['x'], point['y'], point['visibility']
                    cv2.circle(image, (int(x), int(y)), 5, (0, 255, 0), -1)
                temp=correct_angle(candidate,image)  
                image=temp[0]
                
                frame_index += 1
                current_time = frame_index / fps

                direction_camera = refresh_angle(candidate)
                
                #arr1, arr2, arr3, arr4, count = heel(candidate, arr1, arr2, arr3, arr4, image, direction_camera, count)
                Arr, flag = stoop_angle(candidate, Arr, image)
                
                ypositive = ypos(candidate,ypositive)
                lefty = leftfoot(candidate,lefty)
                righty,lower,leftx,rightx = rightfoot(candidate,righty,image,lower,leftx,rightx,direction_camera)

                step_total_fre,touchflag = Calculate_step_frequency(candidate,current_time,array,steps,touchflag,image)
                
                arr = touch1(candidate,arr,image)
                
                forearm_pos = forearm_save(candidate,forearm_pos,direction_camera)
                #arrr = stoop_angle(arrr, arr1, arr2, arr3, arr4)
                
                txt = judge_action(arr, step_total_fre, forearm_pos,arr_time, step_total_fre_time, forearm_pos_time, fps, flag)

                height, width, channel = image.shape
                bytesPerLine = 3 * width
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                qimage = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qimage)
                if (pixmap.height() / pixmap.width()) > (9 / 16):
                    scaled_pixmap = pixmap.scaledToHeight(self.ui.output.height()-5)
                else:
                    scaled_pixmap = pixmap.scaledToWidth(self.ui.output.width()-5)
                scene = QGraphicsScene()
                scene.addPixmap(scaled_pixmap)
                self.ui.output.setScene(scene)
            
                QApplication.processEvents()  # 強制處理事件隊列中的事件
                
                self.ui.spend_time.setText(str(round(current_time)))
                self.ui.step_frequency.setText(str(round(step_total_fre / 5) * 5))
                self.ui.suggestion.setText(str(txt))
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                if self.stop:
                    break
                time.sleep(1/(fps+5))

            print('------------Video Details----------------')
            print('Steps', steps)
            fre = round (step_total_fre)
            print("total_step_fre ",fre)
            print("initial your grade is = ",grade)
            arr,grade = judge_1(grade,arr)
            print("After in part 1 , your grade = ",grade)
            grade = judge2(grade,fre)
            print("After in part 2 , your grade = ",grade)
            print(type(fre))
            grade = judge3(grade,ypositive,forearm_pos,forearm_length)
            print("After in part 3 , your grade = ",grade)
            
            #arrr = stoop_angle(arrr, arr1, arr2, arr3, arr4)
            grade = judge_4(grade, Arr)
            print("After in part 4 , your grade = ",grade)
            grade = balance(grade,bmi,exercise_fre)
            print(f'fps: {video_detail["fps"]}\norigin video length: {video_detail["duration"]}\ntotal_frame: {video_detail["total_frame"]}')

            self.ui.score.setText(str(round(grade,1)))

            end_time = cv2.getTickCount()
            print((end_time - start_time) / cv2.getTickFrequency())
            self.stop = False

    def Stop(self):
        self.stop = True



url = 'http://127.0.0.1:8000/api/'
account = api(url)
app = QApplication([])
SI.Login_Window = Window_Sign_in()
SI.Login_Window.ui.show()
app.exec_()
