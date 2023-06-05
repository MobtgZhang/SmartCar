import sys
import cv2
import requests
from PyQt5.QtGui import QIcon, QPixmap, QImage,QIntValidator
from PyQt5.QtWidgets import  QWidget,QDesktopWidget,QGraphicsScene
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore
import json
import time

class MainApp(QWidget):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = loadUi('interface.ui', self)
        self.windowTitle = "小车调试控制系统"
        self.video_width = 640
        self.video_height = 480
        self.setWindowTitle(self.windowTitle)
        self.timer = QTimer()
        self.timer.timeout.connect(self.openCammera)
        self.setUI()
    def send_message(self,data_dict):
        ip_address = self.textEditIP.toPlainText()
        ip_port = self.textEditControlPort.toPlainText()
        url = "http://{}:{}/login".format(ip_address,ip_port)
        # 通过json方式添加数据
        url = "http://{}:{}/login".format(ip_address,ip_port)
        r = requests.get(url,params={"data":json.dumps(data_dict)})
        if r.status_code!=200:
            self.dispMsg("HTTP ERROR CODE:%d"%r.status_code)
    def keyPressEvent(self, event):
        if self.is_connected:
            key = event.key()
            data_dict = {}
            speed = self.lineEditSpeed.text()
            delay = self.lineEditDelay.text()
            if key == QtCore.Qt.Key_A:
                data_dict["WHEEL-LEFT"] = {
                    "speed":speed,
                    "delay":delay
                }
            if key ==QtCore.Qt.Key_D:
                data_dict["WHEEL-RIGHT"] = {
                    "speed":speed,
                    "delay":delay
                }
            if key ==QtCore.Qt.Key_W:
                data_dict["WHEEL-UP"] = {
                    "speed":speed,
                    "delay":delay
                }
            if key ==QtCore.Qt.Key_S:
                data_dict["WHEEL-DOWN"] = {
                    "speed":speed,
                    "delay":delay
                }
            self.send_message(data_dict)
    def carBushUp(self):
        data_dict = {}
        speed = self.lineEditSpeed.text()
        delay = self.lineEditDelay.text()
        data_dict["WHEEL-UP"] = {
                    "speed":speed,
                    "delay":delay
                }
        self.send_message(data_dict)
    def carBushDown(self):
        data_dict = {}
        speed = self.lineEditSpeed.text()
        delay = self.lineEditDelay.text()
        data_dict["WHEEL-DOWN"] = {
                    "speed":speed,
                    "delay":delay
                }
        self.send_message(data_dict)
    def carBushLeft(self):
        data_dict = {}
        speed = self.lineEditSpeed.text()
        delay = self.lineEditDelay.text()
        data_dict["WHEEL-LEFT"] = {
                    "speed":speed,
                    "delay":delay
                }
        
        self.send_message(data_dict)
    def carBushRight(self):
        data_dict = {}
        speed = self.lineEditSpeed.text()
        delay = self.lineEditDelay.text()
        data_dict["WHEEL-RIGHT"] = {
                    "speed":speed,
                    "delay":delay
                }
        self.send_message(data_dict)
    def steerBushUp(self):
        data_dict = {}
        speed = self.lineEditSpeed.text()
        delay = self.lineEditDelay.text()
        data_dict["STEER-UP"] = {
                    "speed":speed,
                    "delay":delay
                }
        self.send_message(data_dict)
    def steerBushDown(self):
        data_dict = {}
        
        speed = self.lineEditSpeed.text()
        delay = self.lineEditDelay.text()
        data_dict["STEER-DOWN"] = {
                    "speed":speed,
                    "delay":delay
                }
        self.send_message(data_dict)
    def steerBushLeft(self):
        data_dict = {}
        speed = self.lineEditSpeed.text()
        delay = self.lineEditDelay.text()
        data_dict["STEER-LEFT"] = {
                    "speed":speed,
                    "delay":delay
                }
        self.send_message(data_dict)
    def steerBushRight(self):
        data_dict = {}
        speed = self.lineEditSpeed.text()
        delay = self.lineEditDelay.text()
        data_dict["STEER-RIGHT"] = {
                    "speed":speed,
                    "delay":delay
                }
        self.send_message(data_dict)
    def setUI(self):
        self.cameraView = self.ui.cameraView
        # ------------------------------------------------------
        self.carUp = self.ui.carUp
        self.carDown = self.ui.carDown
        self.carLeft = self.ui.carLeft
        self.carRight = self.ui.carRight
        # ------------------------------------------------------
        self.steerDown = self.ui.steerDown
        self.steerRight = self.ui.steerRight
        self.steerLeft = self.ui.steerLeft
        self.steerUp = self.ui.steerUp
        # ------------------------------------------------------
        self.pushButtonConnect = self.ui.pushButtonConnect
        self.pushButtonConnect.clicked.connect(self.connect)
        self.is_connected = False
        self.pushButtonConnect.setText("连接")
        self.pushButtonExit = self.ui.pushButtonExit
        self.pushButtonExit.clicked.connect(self.quit)
        self.pushButtonScreenSpot = self.ui.pushButtonScreenSpot
        self.is_automatic = False
        # ------------------------------------------------------
        self.textEditControlPort = self.ui.textEditControlPort
        self.textEditControlPort.setPlainText("8000")
        self.textEditVideoPort = self.ui.textEditVideoPort
        self.textEditVideoPort.setPlainText("8080")
        self.textEditIP = self.ui.textEditIP
        self.textEditIP.setPlainText("192.168.43.246")
        self.textBrowserStatus = self.ui.textBrowserStatus
        self.lineEditSpeed = self.ui.lineEditSpeed
        # 创建一个整数验证器
        validator = QIntValidator()
        # 设置验证器的范围，这里可以设置允许的最小值和最大值
        validator.setRange(0, 50)
        # 设置验证器到 QLineEdit 中
        self.lineEditSpeed.setValidator(validator)
        self.lineEditSpeed.setText("40")
        self.lineEditSpeed.setEnabled(False)
        self.lineEditDelay = self.ui.lineEditDelay
        # 创建一个整数验证器
        validator = QIntValidator()
        # 设置验证器的范围，这里可以设置允许的最小值和最大值
        validator.setRange(0, 7000)
        # 设置验证器到 QLineEdit 中
        self.lineEditSpeed.setValidator(validator)
        self.lineEditDelay.setEnabled(False)
        self.lineEditDelay.setText("3000")
        self.checkBoxDisplay = self.ui.checkBoxDisplay
        self.checkBoxDisplay.setEnabled(False)
        self.radioButtonAutomatic = self.ui.radioButtonAutomatic
        self.radioButtonAutomatic.setEnabled(False)
        self.radioButtonHand = self.ui.radioButtonHand
        self.radioButtonHand.setEnabled(False)
        self.radioButtonHand.setChecked(True)
        # unnessceary
        self.smartCarLayout = self.ui.smartCarLayout
        self.steerLayout = self.ui.steerLayout
        self.labelControl = self.ui.labelControl
        self.labelControlPort = self.ui.labelControlPort
        self.labelDisplay = self.ui.labelDisplay
        self.labelIP = self.labelIP
        self.labelStatus = self.ui.labelStatus
        self.labelVideoPort = self.ui.labelVideoPort
        self.labelWheelSpeed = self.ui.labelWheelSpeed
        self.labelWheelDelay = self.ui.labelWheelDelay
        self.labelDriveModel = self.ui.labelDriveModel
        self.labelDebugModel = self.ui.labelDebugModel
        # ------------------------------------------------------
        self.center()
    def center(self):
        # 获取屏幕的尺寸信息
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口的尺寸信息
        size = self.geometry()
        # 将窗口移动到指定位置
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
    def closeEvent(self, event):
        self.quit() # 退出程序
    def quit(self):
        self.is_connected = False
        if hasattr(self,"cap_video"):
            self.cap_video.release()
        self.timer.stop()
        sys.exit()
    def connect(self):
        if not self.is_connected:
            ip_address = self.textEditIP.toPlainText()
            ip_port = self.textEditVideoPort.toPlainText()
            cameraid = "http://{}:{}/?action=stream".format(ip_address,ip_port)
            self.cap_video = cv2.VideoCapture(cameraid)
            if not self.cap_video.isOpened():
                self.textBrowserStatus.setPlainText("摄像头连接失败")
            else:
                self.cap_video.set(cv2.CAP_PROP_FRAME_WIDTH,self.video_width)
                self.cap_video.set(cv2.CAP_PROP_FRAME_HEIGHT,self.video_height)
                self.is_connected = True
                self.pushButtonConnect.setText("断开连接")
                self.lineEditSpeed.setEnabled(True)
                self.lineEditDelay.setEnabled(True)
                self.checkBoxDisplay.setEnabled(True)
                self.radioButtonAutomatic.setEnabled(True)
                self.radioButtonHand.setEnabled(True)
                self.timer.start(50)
        else:
            self.is_connected = False
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap(None))
            self.cameraView.setScene(scene)
            self.pushButtonConnect.setText("连接")
            self.lineEditSpeed.setEnabled(False)
            self.lineEditDelay.setEnabled(False)
            self.checkBoxDisplay.setEnabled(False)
            self.radioButtonAutomatic.setEnabled(False)
            self.radioButtonHand.setEnabled(False)
            self.cap_video.release()
            self.timer.stop()
    def openCammera(self):
        ret, frame = self.cap_video.read()
        if ret:
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            frame = cv2.flip(frame, 1, dst=None)
            img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            scene = QGraphicsScene()
            scene.addPixmap(QPixmap(img))
            self.cameraView.setScene(scene)
        else:
            self.is_connected = False
            self.pushButtonConnect.setText("连接")
            self.dispMsg("Failed to capture the video.")
    def dispMsg(self,message):
        message = "[Message]:\t%s"%message
        self.textBrowserStatus.setText(message)
            