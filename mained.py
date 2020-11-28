

import sys
import os
import datetime
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtWidgets import QMainWindow, QFileDialog , QApplication, QShortcut
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import speech_recognition as sr
from pydub import AudioSegment
import simpleaudio as sa
from splited import Ui_MainWindow
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('Splited.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

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
                logger.info('{}'.format(ex)) 
        return text

    def split_time(self, time1, time2, file_out):
        if time1 < time2:
            if time2 > self.duration:
                time2 = self.duration
            newAudio = AudioSegment.from_wav(self.file_in)
            newAudio = newAudio[time1:time2]
            newAudio.export(file_out, format="wav")
            return file_out
    
    def playing(self, file_out_name, time1=None, time2=None, play=True):
        self.split_time(time1, time2, file_out_name+'.wav')        
        wave_obj = sa.WaveObject.from_wave_file(file_out_name+'.wav')
        if play:
            play_obj = wave_obj.play()
            play_obj.wait_done()

class main(Ui_MainWindow):
    
    def __init__(self, win):
        super().__init__()
        self.win  = win
        self.setupUi(win)        
        self.count = 0
        self.timer = QTimer() 
        self.timer.start(100) 
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.slots() 
        self.slots_ShortCut()
        self.slotButtons()
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
        timeing = self.calc()
        self.te_start_subsound.setTime(timeing)
    
    def copy2(self):
        self.mediaPlayer.pause()
        timeing = self.calc()
        self.te_end_subsound.setTime(timeing)

    def open_folder(self):
        options = QFileDialog.Options()
        self.dir_out = QFileDialog.getExistingDirectory(None,
                      caption="Select", directory="G:\\corpus",options=options)
        if self.dir_out:
            self.lbl_save.setText(self.dir_out)
        if self.file_in and self.dir_out:
            self.enable(True)
   
    def open_file(self):
        options = QFileDialog.Options()
        self.file_in, _ = QFileDialog.getOpenFileName(None,
                      caption="Open", directory="G:\\corpus\\audios",options=options)
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
        self.pb_play_subsound.clicked.connect(self.play_subsound)
        self.pb_define_start.clicked.connect(self.copy1)
        self.pb_define_end.clicked.connect(self.copy2)
        self.tb_save_folder.clicked.connect(self.open_folder)
        self.pb_save.clicked.connect(self.save)
        self.timer.timeout.connect(self.showTime) 
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.btn_recal.clicked.connect(self.recal_time)
        self.btn_recal_plus.clicked.connect(self.recal_time_plus)
        self.btn_avance.clicked.connect(self.avance_time)
        self.btn_avance_plus.clicked.connect(self.avance_time_plus)
        self.txte_affichage.textChanged.connect(self.allowSave)
        self.pb_translate_sound.clicked.connect(self.translation)
    
    def slots_ShortCut(self):
        QShortcut(QKeySequence('Ctrl+O'), self.win).activated.connect(self.open_file)
        QShortcut(QKeySequence('Ctrl+F'), self.win).activated.connect(self.open_folder)
        QShortcut(QKeySequence.MoveToPreviousChar, self.win).activated.connect(self.recal_time)
        QShortcut(QKeySequence.MoveToNextChar, self.win).activated.connect(self.avance_time)
        QShortcut(QKeySequence.MoveToPreviousLine, self.win).activated.connect(self.recal_time_plus)
        QShortcut(QKeySequence.MoveToNextLine, self.win).activated.connect(self.avance_time_plus)
        QShortcut(QKeySequence("Return"), self.win).activated.connect(self.play_pause)
        QShortcut(QKeySequence('Ctrl+P'), self.win).activated.connect(self.play_subsound)
        QShortcut(QKeySequence('Ctrl+T'), self.win).activated.connect(self.translation)
        QShortcut(QKeySequence('Ctrl+A'), self.win).activated.connect(self.save)
        
    def play_pause(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.copy2()
        else:
            self.copy1()

    def translation(self):
        
        try:
            if not(os.path.exists(self.dir_out + '\\temp.wav')):
                t = self.te_start_subsound.time()
                t0 = int(t.minute()) * 60000 + int(t.second()) * 1000 + int(t.msec())       
                t = self.te_end_subsound.time()
                t1 = int(t.minute()) * 60000 + int(t.second()) * 1000 + int(t.msec()) 
                self.caption = str(t0) + str(t1)
                self.sp.playing(self.dir_out + '\\temp', t0, t1, False)
            self.my_trans = self.sp.get_text(self.dir_out + '\\temp' + '.wav')
            self.txte_affichage.setText(self.my_trans)
        except Exception as e:
            logger.info('{}'.format(e))

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
        self.sp.playing(self.dir_out + '\\temp', t0, t1, True)
        self.txte_affichage.clear()

    def showTime(self): 
        self.ds_chorono.setValue(self.mediaPlayer.position()/ 1000)
       
    def save(self):
        self.pb_save.setEnabled(False)
        with open(self.dir_out +"\\train_corpus.json", "a", encoding='utf8') as myfile:
            tmp = self.dir_out +'\\temp.wav'
            new = self.dir_out +'\\' + self.caption + '.wav'
            os.rename(tmp, new)
            self.dir_out = self.dir_out.replace('/','\\')
            a = '{"key": '
            b = '\"' + self.dir_out + '\\\\' + self.caption + ".wav\"" + ','
            c = ' "text": '
            d = '\"' + self.txte_affichage.toPlainText() +  '\"}'
            ligne = a + b + c + d + "\n"
            myfile.write(ligne)
        self.txte_affichage.clear()
       
    def keyPressEvent(self, event):
        super(main, self).keyPressEvent(event)
        self.keyPressed.emit(event)
            
    def slotButtons(self):
        self.b_1.clicked.connect(lambda: self.typing(self.b_1))
        self.b_2.clicked.connect(lambda: self.typing(self.b_2))
        self.b_3.clicked.connect(lambda: self.typing(self.b_3))
        self.b_4.clicked.connect(lambda: self.typing(self.b_4))
        self.b_5.clicked.connect(lambda: self.typing(self.b_5))
        self.b_6.clicked.connect(lambda: self.typing(self.b_6))
        self.b_7.clicked.connect(lambda: self.typing(self.b_7))
        self.b_8.clicked.connect(lambda: self.typing(self.b_8))
        self.b_9.clicked.connect(lambda: self.typing(self.b_9))
        self.b_10.clicked.connect(lambda: self.typing(self.b_10))
        self.b_11.clicked.connect(lambda: self.typing(self.b_11))
        self.b_12.clicked.connect(lambda: self.typing(self.b_12))
        self.b_13.clicked.connect(lambda: self.typing(self.b_13))
        self.b_14.clicked.connect(lambda: self.typing(self.b_14))
        self.b_15.clicked.connect(lambda: self.typing(self.b_15))
        self.b_16.clicked.connect(lambda: self.typing(self.b_16))
        self.b_17.clicked.connect(lambda: self.typing(self.b_17))
        self.b_18.clicked.connect(lambda: self.typing(self.b_18))
        self.b_19.clicked.connect(lambda: self.typing(self.b_19))
        self.b_20.clicked.connect(lambda: self.typing(self.b_20))
        self.b_21.clicked.connect(lambda: self.typing(self.b_21))
        self.b_22.clicked.connect(lambda: self.typing(self.b_22))
        self.b_23.clicked.connect(lambda: self.typing(self.b_23))
        self.b_24.clicked.connect(lambda: self.typing(self.b_24))
        self.b_25.clicked.connect(lambda: self.typing(self.b_25))
        self.b_26.clicked.connect(lambda: self.typing(self.b_26))
        self.b_27.clicked.connect(lambda: self.typing(self.b_27))
        self.b_28.clicked.connect(lambda: self.typing(self.b_28))
        self.b_29.clicked.connect(lambda: self.typing(self.b_29))
        self.b_30.clicked.connect(lambda: self.typing(self.b_30))
        self.b_31.clicked.connect(lambda: self.typing(self.b_31))
        self.b_32.clicked.connect(lambda: self.typing(self.b_32))
        self.b_33.clicked.connect(lambda: self.typing(self.b_33))
        self.b_34.clicked.connect(lambda: self.typing(self.b_34))
        self.b_35.clicked.connect(lambda: self.typing(self.b_35))
        self.b_36.clicked.connect(lambda: self.typing(self.b_36))
        self.b_37.clicked.connect(lambda: self.typing(self.b_37))
        self.b_38.clicked.connect(lambda: self.typing(self.b_38))        
        self.b_del.clicked.connect(self.btn_delete)
        self.b_s.clicked.connect(lambda: self.typing(self.b_s))     
     
    def btn_delete(self):
        cursor = self.txte_affichage.textCursor().deletePreviousChar()
        
    def typing(self, btn):
        cursor = self.txte_affichage.textCursor()
        self.txte_affichage.setTextCursor(cursor)
        self.txte_affichage.insertPlainText(btn.text())
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui = main(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#cd "G:/" & G:/Splited/envSplit/Scripts/pyuic5.exe -x "G:/Splited/Splited/splited.ui" -o "G:/Splited/Splited/splited.py"
#pyinstaller --noconfirm --noconsole --onedir --hidden-import tkinter  --exclude-module tkinter "G:/Splited/Splited/mained.py"
