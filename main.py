from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import QThread, QItemSelectionModel, QTimer, Qt, QUrl
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QFileDialog, QMenu , QAction, QApplication
from split import Ui_Split

import wave
import os
import pyglet
from time import sleep         
import threading, time
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import datetime

import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import simpleaudio as sa
import sys

recognizer = sr.Recognizer()

class spliting():
    
    def __init__(self, file_in):
        self.file_in = file_in
        self.duration = len(AudioSegment.from_wav(self.file_in))
    
    def get_text(self, file_ , lang='ar-DZ'):
        text = ''
        with sr.AudioFile(file_) as source:
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio, language=lang)
            except Exception as ex:
                text = str(ex)
        return text

    def split_time(self, time1, time2, file_out):
        # time (millisecond)
        if time1 < time2:
            if time2 > self.duration:
                time2 = self.duration
            newAudio = AudioSegment.from_wav(self.file_in)
            newAudio = newAudio[time1:time2]
            newAudio.export(file_out, format="wav")
            return file_out
    
    def playing(self, file_out_name, time1=None, time2=None):
        self.split_time(time1, time2, file_out_name+'.wav')        
        wave_obj = sa.WaveObject.from_wave_file(file_out_name+'.wav')
        play_obj = wave_obj.play()
        play_obj.wait_done()

class main(QWidget, Ui_Split):

    def __init__(self, win):
        super().__init__()
        self.setupUi(win)
        self.form = QtWidgets.QWidget()
        self.count = 0
        self.timer = QTimer(self) 
        self.timer.start(100) 
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.slots() 
        self.file_in = None
        self.dir_out = None
        self.slider.setEnabled(False)
        self.pb_save.setEnabled(False)
        self.enable(False)

    def enable(self, val):
        self.lbl_duration.setEnabled(val)
        self.btn_recal.setEnabled(val)
        self.btn_recal_plus.setEnabled(val)
        self.pb_define_end.setEnabled(val)
        self.pb_define_start.setEnabled(val)
        self.pb_translate_sound.setEnabled(val)
        self.pb_play_subsound.setEnabled(val)
        self.te_end_subsound.setEnabled(val)
        self.te_start_subsound.setEnabled(val)
        self.ds_chorono.setEnabled(val)
        self.txte_affichage.setEnabled(val)
        self.btn_avance.setEnabled(val)
        self.btn_avance_plus.setEnabled(val)

    def calc(self) :
        self.ds_chorono.setValue(self.mediaPlayer.position()/ 1000)
        val = self.ds_chorono.value() # in seconds
        mun = int(val//60)
        sec = int(val%60)
        mSec = int(((val%60) - sec) * 1000000)
        tm = datetime.time(minute=mun, second=sec,  microsecond=mSec)
        return tm

    def copy1(self):
        self.mediaPlayer.play()
        time = self.calc()
        self.te_start_subsound.setTime(time)
    
    def copy2(self):
        self.mediaPlayer.pause()
        time = self.calc()
        self.te_end_subsound.setTime(time)

    def open_folder(self):
        options = QtWidgets.QFileDialog.Options()
        self.dir_out = QtWidgets.QFileDialog.getExistingDirectory(None,
                      caption="Select", directory="G:\\",options=options)
        if self.dir_out:
            self.lbl_save.setText(self.dir_out)
        if self.file_in and self.dir_out:
            self.enable(True)
   
    def open_file(self):
        options = QtWidgets.QFileDialog.Options()
        self.file_in, _ = QtWidgets.QFileDialog.getOpenFileName(None,
                      caption="Open", directory="G:\\",options=options)
        if self.file_in:
            self.lbl_file.setText(self.file_in)
            self.sp = spliting(self.file_in)
            self.lbl_duration.setText(str(self.sp.duration))
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.file_in)))
            self.slider.setMaximum(self.sp.duration)
        if self.file_in and self.dir_out:
            self.enable(True)
    
    def slots(self):
        self.btn_open.clicked.connect(self.open_file)
        #self.pb_play_sound.clicked.connect(self.play_video)     
        self.pb_play_subsound.clicked.connect(self.play_subsound)
        self.pb_define_start.clicked.connect(self.copy1)
        self.pb_define_end.clicked.connect(self.copy2)
        self.tb_save_folder.clicked.connect(self.open_folder)
        self.pb_save.clicked.connect(self.save)
        #self.slider.sliderMoved.connect(self.set_position)
        #self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.timer.timeout.connect(self.showTime) 
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.btn_recal.clicked.connect(self.recal_time)
        self.btn_recal_plus.clicked.connect(self.recal_time_plus)
        self.btn_avance.clicked.connect(self.avance_time)
        self.btn_avance_plus.clicked.connect(self.avance_time_plus)
        self.txte_affichage.textChanged.connect(self.allowSave)
        self.pb_translate_sound.clicked.connect(self.translation)
    
    def translation(self):
        self.my_trans = self.sp.get_text(self.dir_out + '//temp' + '.wav')
        self.txte_affichage.setText(self.my_trans)

    def allowSave(self):
        if self.txte_affichage.toPlainText()!= '':
            self.pb_save.setEnabled(True)
        else: 
            self.pb_save.setEnabled(False)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)
    
    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def recal_time(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() - 100)
        self.ds_chorono.setValue(self.mediaPlayer.position()/ 1000)

    def recal_time_plus(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() - 1000)
        self.ds_chorono.setValue(self.mediaPlayer.position()/ 1000)
    
    def avance_time(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() + 100)
        self.ds_chorono.setValue(self.mediaPlayer.position()/ 1000)
    
    def avance_time_plus(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() + 1000)
        self.ds_chorono.setValue(self.mediaPlayer.position()/ 1000)
               
    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause() 
            self.ds_chorono.setValue(self.mediaPlayer.position()/ 1000)
        else:
            self.mediaPlayer.play()
        
    def play_subsound(self):        
        t = self.te_start_subsound.time()
        t0 = int(t.minute()) * 60000 + int(t.second()) * 1000 + int(t.msec())       
        t = self.te_end_subsound.time()
        t1 = int(t.minute()) * 60000 + int(t.second()) * 1000 + int(t.msec()) 
        self.caption = str(t0) + str(t1)
        self.sp.playing(self.dir_out + '//temp', t0, t1)
        self.txte_affichage.clear()

    def showTime(self): 
        self.ds_chorono.setValue(self.mediaPlayer.position()/ 1000)
       
    def save(self):
        with open(self.dir_out +"//corpus.txt", "a", encoding='utf8') as myfile:
            tmp = self.dir_out +'//temp.wav'
            new = self.dir_out +'//' + self.caption + '.wav'
            os.rename(tmp, new)
            ligne = '\"' + self.caption + ".wav\"" + ',' + '\"' + self.my_trans +  '\"' + "\n"
            myfile.write(ligne)
       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = main(Form)
    Form.show()
    sys.exit(app.exec_())

#cd "G:/" & G:/Splited/envs/Scripts/pyuic5.exe -x "G:/Splited/Splited/split.ui" -o "G:/Splited/Splited/split.py"