# importing libraries 
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys 
  
class Window(QMainWindow): 
  
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Python Stop watch") 
        self.setGeometry(100, 100, 400, 500) 
        self.UiComponents() 
        self.show() 
  
    def UiComponents(self): 
        self.count = 0
        self.flag = False
        self.label = QLabel(self) 
        self.label.setGeometry(75, 100, 250, 70) 
        self.label.setStyleSheet("border : 4px solid black;") 
        self.label.setText(str(self.count)) 
        self.label.setFont(QFont('Arial', 25)) 
        self.label.setAlignment(Qt.AlignCenter) 
        start = QPushButton("Start", self) 
        start.setGeometry(125, 250, 150, 40) 
        start.pressed.connect(self.Start) 
        pause = QPushButton("Pause", self) 
        pause.setGeometry(125, 300, 150, 40) 
        pause.pressed.connect(self.Pause) 
        re_set = QPushButton("Re-set", self) 
        re_set.setGeometry(125, 350, 150, 40) 
        re_set.pressed.connect(self.Re_set) 
        timer = QTimer(self) 
        timer.timeout.connect(self.showTime) 
        timer.start(100) 
  
    def showTime(self): 
        if self.flag:  
            self.count+= 1
        text = str(self.count / 10) 
        self.label.setText(text) 
  
    def Start(self): 
        self.flag = True
  
    def Pause(self): 
        self.flag = False
  
    def Re_set(self): 
        self.flag = False
        self.count = 0
        self.label.setText(str(self.count)) 
  
 
App = QApplication(sys.argv) 
window = Window() 
sys.exit(App.exec()) 