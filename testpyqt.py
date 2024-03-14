import sys
import Data_api.account_api as api
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.account=api.accountAPI('http://127.0.0.1:8000/api/')

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Run")

        self.main_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.main_widget)

        self.stacked_layout = QtWidgets.QStackedLayout()
        self.main_widget.setLayout(self.stacked_layout)

        # 添加登入頁面
        self.signin_page = QtWidgets.QWidget()
        self.stacked_layout.addWidget(self.signin_page)

        self.username_label = QtWidgets.QLabel("Username")
        self.username_edit = QtWidgets.QLineEdit()

        self.password_label = QtWidgets.QLabel("Password")
        self.password_edit = QtWidgets.QLineEdit()

        self.signin_button = QtWidgets.QPushButton("Sign In")
        self.signin_button.clicked.connect(self.on_signin_clicked)
        self.signup_button = QtWidgets.QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.on_signup_clicked)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_edit)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_edit)
        self.layout.addWidget(self.signin_button)
        self.layout.addWidget(self.signup_button)

        self.signin_page.setLayout(self.layout)

        # 添加個人資訊頁面
        self.update_profile_page = QtWidgets.QWidget()
        self.stacked_layout.addWidget(self.update_profile_page)

        self.birthdate_label = QtWidgets.QLabel("Birthdate")
        self.birthdate_edit = QtWidgets.QDateEdit()

        self.height_label = QtWidgets.QLabel("Height")
        self.height_edit = QtWidgets.QLineEdit()

        self.weight_label = QtWidgets.QLabel("Weight")
        self.weight_edit = QtWidgets.QLineEdit()


        self.switch_button = QtWidgets.QPushButton("Switch")
        self.switch_button.clicked.connect(self.on_switch_clicked)

        self.update_button = QtWidgets.QPushButton("update")
        self.update_button.clicked.connect(self.on_update_clicked)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.birthdate_label)
        self.layout.addWidget(self.birthdate_edit)
        self.layout.addWidget(self.height_label)
        self.layout.addWidget(self.height_edit)
        self.layout.addWidget(self.weight_label)
        self.layout.addWidget(self.weight_edit)
        self.layout.addWidget(self.switch_button)
        self.layout.addWidget(self.update_button)

        self.update_profile_page.setLayout(self.layout)

        # 添加Rank頁面
        self.rank_page = QtWidgets.QWidget()
        self.stacked_layout.addWidget(self.rank_page)

        self.label1 = QtWidgets.QLabel("                  Name")
        self.label2=QtWidgets.QLabel("                    Score")

        self.order1 = QtWidgets.QLabel("1")
        self.order2 = QtWidgets.QLabel("2")
        self.order3 = QtWidgets.QLabel("3")

        self.name1 = QtWidgets.QLabel("XXX")
        self.name2 = QtWidgets.QLabel("YYY")
        self.name3 = QtWidgets.QLabel("ZZZ")


        self.signin_button = QtWidgets.QPushButton("Sign In")
        self.signin_button.clicked.connect(self.on_signin_clicked)
        self.signup_button = QtWidgets.QPushButton("Sign Up")

        self.h_layout=QtWidgets.QHBoxLayout()
        self.h_layout.addWidget(self.label1)
        self.h_layout.addWidget(self.label2)

        self.h1_layout=QtWidgets.QHBoxLayout()
        self.h1_layout.addWidget(self.order1)
        self.h1_layout.addWidget(self.name1)

        self.h2_layout=QtWidgets.QHBoxLayout()
        self.h2_layout.addWidget(self.order2)
        self.h2_layout.addWidget(self.name2)

        self.h3_layout=QtWidgets.QHBoxLayout()
        self.h3_layout.addWidget(self.order3)
        self.h3_layout.addWidget(self.name3)

        widgeth=QtWidgets.QWidget()
        widgeth.setLayout(self.h_layout)

        widget1 = QtWidgets.QWidget()
        widget1.setLayout(self.h1_layout)

        widget2 = QtWidgets.QWidget()
        widget2.setLayout(self.h2_layout)

        widget3 = QtWidgets.QWidget()
        widget3.setLayout(self.h3_layout)

        self.myrank=QtWidgets.QLabel("My Rank: 1000名")
        self.return_button=QtWidgets.QPushButton("return")
        self.return_button.clicked.connect(self.on_return_clicked)

        self.main_layout=QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(widgeth)
        self.main_layout.addWidget(widget1)  
        self.main_layout.addWidget(widget2)
        self.main_layout.addWidget(widget3)
        self.main_layout.addWidget(self.myrank)
        self.main_layout.addWidget(self.return_button)


        self.rank_page.setLayout(self.main_layout)

        #主頁面
        self.home_page=QtWidgets.QWidget()
        self.stacked_layout.addWidget(self.home_page)
        self.detect_button=QtWidgets.QPushButton("Run Detect")
        self.detect_button.clicked.connect(self.on_rundetect_clicked)
        self.rank_button=QtWidgets.QPushButton("Rank")
        self.rank_button.clicked.connect(self.on_rank_clicked)
        self.update_information_button=QtWidgets.QPushButton("Information update")
        self.update_information_button.clicked.connect(self.on_update_information_clicked)

        self.information_button=QtWidgets.QPushButton("Information")
        self.information_button.clicked.connect(self.on_information_clicked)


        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.detect_button)
        self.layout.addWidget(self.rank_button)
        self.layout.addWidget(self.update_information_button)
        self.layout.addWidget(self.information_button)

        self.home_page.setLayout(self.layout)

        #顯示個人資料頁面
        self.profile_page = QtWidgets.QWidget()
        self.stacked_layout.addWidget(self.profile_page)

        if self.account.get_account_detail() is not None:
            data = self.account.get_account_detail().json()
            self.name_label = QtWidgets.QLabel("Name")
            self.name_show = QtWidgets.QLabel(data.get('username'))

            self.birthdate_label = QtWidgets.QLabel("Birthdate")
            self.birthdate_show = QtWidgets.QLabel(data.get('born'))

            self.height_label = QtWidgets.QLabel("Height")
            self.height_show = QtWidgets.QLabel(str(data.get('height')))

            self.weight_label = QtWidgets.QLabel("Weight")
            self.weight_show = QtWidgets.QLabel(str(data.get('weight')))

            self.switch_button = QtWidgets.QPushButton("Switch")
            self.switch_button.clicked.connect(self.on_switch_clicked)

            # 创建一个新的布局变量，以避免覆盖之前的布局变量
            profile_layout = QtWidgets.QVBoxLayout()
            profile_layout.addWidget(self.name_label)
            profile_layout.addWidget(self.name_show)
            profile_layout.addWidget(self.birthdate_label)
            profile_layout.addWidget(self.birthdate_show)
            profile_layout.addWidget(self.height_label)
            profile_layout.addWidget(self.height_show)
            profile_layout.addWidget(self.weight_label)
            profile_layout.addWidget(self.weight_show)
            profile_layout.addWidget(self.switch_button)

            # 将新的布局设置给个人信息页面
            self.profile_page.setLayout(profile_layout)


        # 顯示頁面
        self.stacked_layout.setCurrentIndex(0)

    def on_update_clicked(self,data):
        height = self.height_edit.text()
        weight = self.weight_edit.text()
        born = self.birthdate_edit.date().toString(QtCore.Qt.ISODate)

        data = {'height': height, 'weight': weight, 'born': born}
        print('pyqt', data)
        self.account.update_information(data)
    
    def on_information_clicked(self):
        if self.account.get_account_detail() is not None:
            data = self.account.get_account_detail().json()
            self.height_show.setText(str(data.get('height')))
            self.weight_show.setText(str(data.get('weight')))
            self.update()
        self.stacked_layout.setCurrentIndex(4)

    def on_return_clicked(self):
        self.stacked_layout.setCurrentIndex(3)
    
    def on_rundetect_clicked(self):
        pass

    def on_rank_clicked(self):
        self.stacked_layout.setCurrentIndex(2)

    def on_update_information_clicked(self):
        self.stacked_layout.setCurrentIndex(1)

    def on_signin_clicked(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        print(username,password)
        if username is not None and password is not None:
            response=self.account.login(username,password)
            if response.status_code==200:
                self.stacked_layout.setCurrentIndex(3)

    def on_signup_clicked(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        if username is not None and password is not None:
            response=self.account.register(username,password)
            if response.status_code==201:
                print('Now you can login n')

    def on_switch_clicked(self):
        # 切換到登入頁面或個人資訊頁面
        self.stacked_layout.setCurrentIndex(3)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
