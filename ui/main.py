from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader

import requests

from lib.share import Share_Info as SI
class Window_Sign_in:

    def __init__(self):
        #self.url = url
        self.ui = QUiLoader().load('Sign_in.ui')
        self.ui.log_in.clicked.connect(self.Log_in)
        self.ui.sign_up.clicked.connect(self.Sign_up)
        self.ui.password.returnPressed.connect(self.Log_in)


    def Log_in(self):
        #username = self.ui.username.text().strip()
        #password = self.ui.password.text().strip()

        #url = self.url + 'login/'
        #response = requests.Session().post(url,json = {
        #    "username" : username,
        #    "password" : password,
        #})

        #if response.status_code!=200:
        #    QMessageBox.warning(
        #        self.ui,
        #        'Failed',
        #        'response.json().get('error')')
        #    return
        #else:
        #    QMessageBox.information(
        #        self.ui,
        #        'Successful',
        #        'response.json().get('message')')

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
        self.ui = QUiLoader().load('Home.ui')
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
        #self.url = url
        self.ui = QUiLoader().load('Sign_up.ui')
        self.ui.back.clicked.connect(self.Back)
        self.ui.Register.clicked.connect(self.Register)

    def Back(self):
        SI.Login_Window.ui.show()
        self.ui.close()

    def Register(self):
        name = self.ui.name.text().strip()
        born = self.ui.born.text().strip()
        height = self.ui.Height.text().strip()
        weight = self.ui.weight.text().strip()
        username = self.ui.username.text().strip()
        password = self.ui.password.text().strip()

        #url = self.url + 'register/'
        #response = requests.Session().post(url,json = {
        #    "username" : username,
        #    "password" : password,
        #})

        #if response.status_code!=201:
        #    QMessageBox.warning(
        #        self.ui,
        #        'Failed',
        #        'response.json().get('error')')
        #    return
        #else:
        #    QMessageBox.information(
        #        self.ui,
        #        'Successful',
        #        'response.json().get('message')')

        SI.Login_Window = Window_Sign_in()
        SI.Login_Window.ui.show()
        self.ui.close()

class Window_Information :

    def __init__(self):
        self.ui = QUiLoader().load('Information.ui')
        self.ui.back.clicked.connect(self.Back)
        self.ui.Update.clicked.connect(self.Update)
        self.ui.log_out.clicked.connect(self.Log_out)
        #url = self.url + 'information/'
        #response = requests.Session().get(url)
        #if response.status_code==400:
        #    QMessageBox.warning(
        #        self.ui,
        #        'Failed',
        #        'response.json().get('error')')
        #    return
        #elif response.status_code==200:
        #    self.ui.name.setText(response.json().get('name'))
        #    self.ui.born.setText(response.json().get('born'))
        #    self.ui.Height.setText(response.json().get('height'))
        #    self.ui.weight.setText(response.json().get('weight'))
        #    self.ui.username.setText(response.json().get('username'))
        #    self.ui.score.setText(response.json().get('score'))
        #    self.ui.distance.setText(response.json().get('distance'))
        #    self.ui.spend_time.setText(response.json().get('spend_time'))

    def Back(self):
        SI.Home_Window.ui.show()
        self.ui.close()

    def Update(self):
        SI.Update_Information_Window.ui.show()
        self.ui.close()
    
    def Log_out(self):
        #url=self.url+'logout/'
        #response=requests.Session().get(url)
        #if response.status_code==200:
        #    QMessageBox.information(
        #        self.ui,
        #        'Successful',
        #        'response.json().get('message')')
        #else:
        #    QMessageBox.warning(
        #        self.ui,
        #        'Failed',
        #        'response.json().get('error')')
        #    return
        SI.Login_Window.ui.show()
        self.ui.close()
        
class Window_Update_Information :
    
    def __init__(self):
        self.ui = QUiLoader().load('Update_Information.ui')
        self.ui.back.clicked.connect(self.Back)
        self.ui.save.clicked.connect(self.Save)

    def Back(self):
        SI.Information_Window.ui.show()
        self.ui.close()

    def Save(self):
        born = self.ui.born.text().strip()
        height = self.ui.height.text().strip()
        weight = self.ui.weight.text().strip()
        #url = self.url + 'information/'
        #response = requests.Session().post(url,json = {
        #    "born" : born,
        #    "height" : height,
        #    "weight" : weight
        #})

        #if response.status_code!=200:
        #    QMessageBox.warning(
        #        self.ui,
        #        'Failed',
        #        'response.json().get('error')')
        #    return
        #else:
        #    QMessageBox.information(
        #        self.ui,
        #        'Successful',
        #        'response.json().get('message')')
        SI.Information_Window.ui.show()
        self.ui.close()

class Window_Rank :

    def __init__(self):
        self.ui = QUiLoader().load('Rank.ui')
        self.ui.back.clicked.connect(self.Back)
        #url = self.url + 'information/'
        #response = requests.Session().get(url)
        #if response.status_code==400:
        #    QMessageBox.warning(
        #        self.ui,
        #        'Failed',
        #        'response.json().get('error')')
        #    return
        #elif response.status_code==200:
        #    self.ui.current_ranking.setText(response.json().get('rank'))

        #url = self.url + 'rank/'
        #response = requests.Session().get(url)
        #if response.status_code!=200:
        #    QMessageBox.warning(
        #        self.ui,
        #        'Failed',
        #        'response.json().get('error')')
        #    return
        #else:
        #    self.ui.first_name.setText(response.json().get('first_name'))
        #    self.ui.first_score.setText(response.json().get('first_score'))
        #    self.ui.second_name.setText(response.json().get('second_name'))
        #    self.ui.second_score.setText(response.json().get('second_score'))
        #    self.ui.third_name.setText(response.json().get('third_name'))
        #    self.ui.third_score.setText(response.json().get('third_score'))
        #    self.ui.fourth_name.setText(response.json().get('fourth_name'))
        #    self.ui.fourth_score.setText(response.json().get('fourth_score'))
        #    self.ui.fifth_name.setText(response.json().get('fifth_name'))
        #    self.ui.fifth_score.setText(response.json().get('fifth_score'))
        #    self.ui.sixth_name.setText(response.json().get('sixth_name'))
        #    self.ui.sixth_score.setText(response.json().get('sixth_score'))
        #    self.ui.seventh_name.setText(response.json().get('seventh_name'))
        #    self.ui.seventh_score.setText(response.json().get('seventh_score'))
        #    self.ui.eighth_name.setText(response.json().get('eighth_name'))
        #    self.ui.eighth_score.setText(response.json().get('eighth_score'))
        #    self.ui.ninth_name.setText(response.json().get('ninth_name'))
        #    self.ui.ninth_score.setText(response.json().get('ninth_score'))
        #    self.ui.tenth_name.setText(response.json().get('tenth_name'))
        #    self.ui.tenth_score.setText(response.json().get('tenth_score'))

    def Back(self):
        SI.Home_Window.ui.show()
        self.ui.close()

class Window_Run_detect :

    def __init__(self):
        self.ui = QUiLoader().load('Run_detect.ui')
        self.ui.back.clicked.connect(self.Back)
        self.ui.start.clicked.connect(self.Start)
        self.ui.filepath.returnPressed.connect(self.filepath)

    def Back(self):
        SI.Home_Window.ui.show()
        self.ui.close()

    def Start(self):
        filepath = self.ui.filepath.text().strip()
        #Coming Soon

    def filepath(self):
        pass
        #Coming Soon

class Window_Activity :
    
    def __init__(self):
        self.ui = QUiLoader().load('Activity.ui')
        self.ui.back.clicked.connect(self.Back)
        self.ui.search.clicked.connect(self.Search)
        self.ui.previous_photo.clicked.connect(self.Previous_photo)
        self.ui.next_photo.clicked.connect(self.Next_photo)
    
    def Back(self):
        SI.Home_Window.ui.show()
        self.ui.close()

    def Search(self):
        date1 = self.ui.date1.text().strip()
        date2 = self.ui.date2.text().strip()
        #Coming Soon

    def Previous_photo(self):
        pass
        #Coming Soon

    def Next_photo(self):
        pass
        #Coming Soon


app = QApplication([])
SI.Login_Window = Window_Sign_in()
SI.Login_Window.ui.show()
app.exec_()