from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import QThread, QItemSelectionModel, QTimer, Qt, QUrl
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QFileDialog, QMenu , QAction, QApplication
from split import Ui_Split

import pyaudio
import wave
from os import path
import pyglet
from time import sleep         
from spliting import spliting
import threading, time
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class main(QWidget, Ui_Split):

    def __init__(self, win):
        super().__init__()
        self.setupUi(win)
        self.form = QtWidgets.QWidget()
        self.count = 0
        self.flag = False
        self.timer = QTimer(self) 
        self.timer.start(100) 
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        #self.th = threading.Thread(target=self.playStream)
        
        self.slots() 
        
    def copy1(self):
        self.te_start_subsound.setTime(self.te_sound.time())
    
    def copy2(self):
        self.te_end_subsound.setTime(self.te_sound.time())
    
    def slots(self):
        self.btn_open.clicked.connect(self.open_file)
        self.pb_play_sound.clicked.connect(self.play_video)     
        self.pb_play_subsound.clicked.connect(self.play_subsound)
        self.pb_pause_sound.clicked.connect(self.set_position)
        self.pb_define_start.clicked.connect(self.copy1)
        self.pb_define_end.clicked.connect(self.copy2)
        self.tb_save_folder.clicked.connect(self.open_folder)
        self.pb_save.clicked.connect(self.save)
        self.timer.timeout.connect(self.showTime) 
    
    def save(self):
        with open("test.txt", "a", encoding='utf8') as myfile:
            myfile.write(self.caption + "," + self.my_trans + "\n")
            
    def pause_subsound(self):
        pass

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause() 
            self.flag = False
        else:
            self.flag = True
            self.mediaPlayer.play()

    def play_subsound(self):        
        t = self.te_start_subsound.time()
        t0 = (int(t.minute()) * 60000) + (int(t.second()) * 1000)        
        t = self.te_end_subsound.time()
        t1 = (int(t.minute()) * 60000) + (int(t.second()) * 1000)
        self.caption = str(t0) + str(t1)
        self.sp.playing(self.file_in, self.caption, t0, t1)
        self.txte_affichage.clear()
        self.pb_save.setEnabled(False)
        self.my_trans = self.sp.get_text(self.caption + '.wav')
        self.txte_affichage.setText(self.my_trans)
        self.pb_save.setEnabled(True)

    def open_folder(self):
        options = QtWidgets.QFileDialog.Options()
        self.dir_out = QtWidgets.QFileDialog.getExistingDirectory(None,
                      caption="Select", directory="C:\\",options=options)
        self.lbl_save.setText(self.dir_out)
   
    def open_file(self):
        options = QtWidgets.QFileDialog.Options()
        self.file_in, _ = QtWidgets.QFileDialog.getOpenFileName(None,
                      caption="Open", directory="C:\\",options=options)
        self.lbl_file.setText(self.file_in)
        self.sp = spliting(self.file_in)
        self.wf = wave.open(self.file_in, 'rb')
        self.pyaud = pyaudio.PyAudio()
        self.strm = self.pyaud.open(format=self.pyaud.get_format_from_width(self.wf.getsampwidth()),
                          channels=self.wf.getnchannels(), rate=self.wf.getframerate(), output=True)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.file_in)))


    def showTime(self): 
        if self.flag:  
            self.count+= 1
        text = str(self.count / 10) 
        self.label.setText(text)

    def set_position(self, position=5000):
        self.mediaPlayer.setPosition(position)            
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = main(Form)
    Form.show()
    sys.exit(app.exec_())

#cd "G:/" & G:/Splited/envs/Scripts/pyuic5.exe -x "G:/Splited/split.ui" -o "G:/Splited/split.py"
