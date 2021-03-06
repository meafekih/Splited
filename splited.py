# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:/Splited/Splited/splited.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(3)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.btn_open = QtWidgets.QPushButton(self.frame_2)
        self.btn_open.setObjectName("btn_open")
        self.gridLayout.addWidget(self.btn_open, 1, 1, 1, 1)
        self.lbl_file = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_file.setFont(font)
        self.lbl_file.setText("")
        self.lbl_file.setObjectName("lbl_file")
        self.gridLayout.addWidget(self.lbl_file, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        self.tb_save_folder = QtWidgets.QPushButton(self.frame_2)
        self.tb_save_folder.setObjectName("tb_save_folder")
        self.gridLayout.addWidget(self.tb_save_folder, 2, 1, 1, 1)
        self.lbl_save = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_save.setFont(font)
        self.lbl_save.setText("")
        self.lbl_save.setObjectName("lbl_save")
        self.gridLayout.addWidget(self.lbl_save, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_avance = QtWidgets.QToolButton(self.frame)
        self.btn_avance.setObjectName("btn_avance")
        self.gridLayout_2.addWidget(self.btn_avance, 3, 3, 1, 1)
        self.btn_recal_plus = QtWidgets.QToolButton(self.frame)
        self.btn_recal_plus.setObjectName("btn_recal_plus")
        self.gridLayout_2.addWidget(self.btn_recal_plus, 3, 0, 1, 1)
        self.btn_avance_plus = QtWidgets.QToolButton(self.frame)
        self.btn_avance_plus.setObjectName("btn_avance_plus")
        self.gridLayout_2.addWidget(self.btn_avance_plus, 3, 4, 1, 1)
        self.ds_chorono = QtWidgets.QDoubleSpinBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ds_chorono.setFont(font)
        self.ds_chorono.setDecimals(3)
        self.ds_chorono.setMaximum(3600.0)
        self.ds_chorono.setSingleStep(0.1)
        self.ds_chorono.setObjectName("ds_chorono")
        self.gridLayout_2.addWidget(self.ds_chorono, 3, 2, 1, 1)
        self.slider = QtWidgets.QSlider(self.frame)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.gridLayout_2.addWidget(self.slider, 0, 0, 1, 6)
        self.lbl_duration = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_duration.setFont(font)
        self.lbl_duration.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbl_duration.setText("")
        self.lbl_duration.setObjectName("lbl_duration")
        self.gridLayout_2.addWidget(self.lbl_duration, 3, 5, 1, 1)
        self.pb_play_subsound = QtWidgets.QPushButton(self.frame)
        self.pb_play_subsound.setObjectName("pb_play_subsound")
        self.gridLayout_2.addWidget(self.pb_play_subsound, 7, 0, 1, 3)
        self.btn_recal = QtWidgets.QToolButton(self.frame)
        self.btn_recal.setObjectName("btn_recal")
        self.gridLayout_2.addWidget(self.btn_recal, 3, 1, 1, 1)
        self.pb_define_start = QtWidgets.QPushButton(self.frame)
        self.pb_define_start.setObjectName("pb_define_start")
        self.gridLayout_2.addWidget(self.pb_define_start, 5, 0, 1, 3)
        self.te_start_subsound = QtWidgets.QTimeEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.te_start_subsound.setFont(font)
        self.te_start_subsound.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.te_start_subsound.setObjectName("te_start_subsound")
        self.gridLayout_2.addWidget(self.te_start_subsound, 5, 3, 1, 3)
        self.te_end_subsound = QtWidgets.QTimeEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.te_end_subsound.setFont(font)
        self.te_end_subsound.setObjectName("te_end_subsound")
        self.gridLayout_2.addWidget(self.te_end_subsound, 6, 3, 1, 3)
        self.pb_translate_sound = QtWidgets.QPushButton(self.frame)
        self.pb_translate_sound.setObjectName("pb_translate_sound")
        self.gridLayout_2.addWidget(self.pb_translate_sound, 7, 3, 1, 3)
        self.pb_define_end = QtWidgets.QPushButton(self.frame)
        self.pb_define_end.setObjectName("pb_define_end")
        self.gridLayout_2.addWidget(self.pb_define_end, 6, 0, 1, 3)
        self.verticalLayout.addWidget(self.frame)
        self.split_frame = QtWidgets.QFrame(self.centralwidget)
        self.split_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.split_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.split_frame.setLineWidth(3)
        self.split_frame.setObjectName("split_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.split_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.split_frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pb_save = QtWidgets.QPushButton(self.frame_3)
        self.pb_save.setObjectName("pb_save")
        self.gridLayout_4.addWidget(self.pb_save, 4, 15, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 4, 0, 1, 7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 4, 12, 1, 3)
        self.b_10 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_10.setFont(font)
        self.b_10.setObjectName("b_10")
        self.gridLayout_4.addWidget(self.b_10, 0, 5, 1, 1)
        self.b_5 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_5.setFont(font)
        self.b_5.setObjectName("b_5")
        self.gridLayout_4.addWidget(self.b_5, 0, 10, 1, 1)
        self.b_11 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_11.setFont(font)
        self.b_11.setObjectName("b_11")
        self.gridLayout_4.addWidget(self.b_11, 0, 4, 1, 1)
        self.b_7 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_7.setFont(font)
        self.b_7.setObjectName("b_7")
        self.gridLayout_4.addWidget(self.b_7, 0, 8, 1, 1)
        self.b_12 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_12.setFont(font)
        self.b_12.setObjectName("b_12")
        self.gridLayout_4.addWidget(self.b_12, 0, 3, 1, 1)
        self.b_del = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_del.setFont(font)
        self.b_del.setObjectName("b_del")
        self.gridLayout_4.addWidget(self.b_del, 0, 15, 1, 1)
        self.b_1 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_1.setFont(font)
        self.b_1.setObjectName("b_1")
        self.gridLayout_4.addWidget(self.b_1, 0, 14, 1, 1)
        self.b_31 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_31.setFont(font)
        self.b_31.setObjectName("b_31")
        self.gridLayout_4.addWidget(self.b_31, 2, 6, 1, 1)
        self.b_3 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_3.setFont(font)
        self.b_3.setObjectName("b_3")
        self.gridLayout_4.addWidget(self.b_3, 0, 12, 1, 1)
        self.b_4 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_4.setFont(font)
        self.b_4.setObjectName("b_4")
        self.gridLayout_4.addWidget(self.b_4, 0, 11, 1, 1)
        self.b_16 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_16.setFont(font)
        self.b_16.setObjectName("b_16")
        self.gridLayout_4.addWidget(self.b_16, 1, 11, 1, 1)
        self.b_14 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_14.setFont(font)
        self.b_14.setObjectName("b_14")
        self.gridLayout_4.addWidget(self.b_14, 1, 13, 1, 1)
        self.b_25 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_25.setFont(font)
        self.b_25.setObjectName("b_25")
        self.gridLayout_4.addWidget(self.b_25, 2, 12, 1, 1)
        self.b_17 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_17.setFont(font)
        self.b_17.setObjectName("b_17")
        self.gridLayout_4.addWidget(self.b_17, 1, 10, 1, 1)
        self.b_2 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_2.setFont(font)
        self.b_2.setObjectName("b_2")
        self.gridLayout_4.addWidget(self.b_2, 0, 13, 1, 1)
        self.b_15 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_15.setFont(font)
        self.b_15.setObjectName("b_15")
        self.gridLayout_4.addWidget(self.b_15, 1, 12, 1, 1)
        self.b_19 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_19.setFont(font)
        self.b_19.setObjectName("b_19")
        self.gridLayout_4.addWidget(self.b_19, 1, 8, 1, 1)
        self.b_21 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_21.setFont(font)
        self.b_21.setObjectName("b_21")
        self.gridLayout_4.addWidget(self.b_21, 1, 6, 1, 1)
        self.b_18 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_18.setFont(font)
        self.b_18.setObjectName("b_18")
        self.gridLayout_4.addWidget(self.b_18, 1, 9, 1, 1)
        self.b_20 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_20.setFont(font)
        self.b_20.setObjectName("b_20")
        self.gridLayout_4.addWidget(self.b_20, 1, 7, 1, 1)
        self.b_22 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_22.setFont(font)
        self.b_22.setObjectName("b_22")
        self.gridLayout_4.addWidget(self.b_22, 1, 5, 1, 1)
        self.b_34 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_34.setFont(font)
        self.b_34.setObjectName("b_34")
        self.gridLayout_4.addWidget(self.b_34, 3, 11, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 1, 14, 1, 2)
        self.b_23 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_23.setFont(font)
        self.b_23.setObjectName("b_23")
        self.gridLayout_4.addWidget(self.b_23, 1, 4, 1, 1)
        self.b_24 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_24.setFont(font)
        self.b_24.setObjectName("b_24")
        self.gridLayout_4.addWidget(self.b_24, 1, 3, 1, 1)
        self.b_30 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_30.setFont(font)
        self.b_30.setObjectName("b_30")
        self.gridLayout_4.addWidget(self.b_30, 2, 7, 1, 1)
        self.b_35 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_35.setFont(font)
        self.b_35.setObjectName("b_35")
        self.gridLayout_4.addWidget(self.b_35, 3, 10, 1, 1)
        self.b_37 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_37.setFont(font)
        self.b_37.setObjectName("b_37")
        self.gridLayout_4.addWidget(self.b_37, 3, 8, 1, 1)
        self.b_33 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_33.setFont(font)
        self.b_33.setObjectName("b_33")
        self.gridLayout_4.addWidget(self.b_33, 2, 4, 1, 1)
        self.b_38 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_38.setFont(font)
        self.b_38.setObjectName("b_38")
        self.gridLayout_4.addWidget(self.b_38, 3, 7, 1, 1)
        self.b_36 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_36.setFont(font)
        self.b_36.setObjectName("b_36")
        self.gridLayout_4.addWidget(self.b_36, 3, 9, 1, 1)
        self.b_28 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_28.setFont(font)
        self.b_28.setObjectName("b_28")
        self.gridLayout_4.addWidget(self.b_28, 2, 9, 1, 1)
        self.b_6 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_6.setFont(font)
        self.b_6.setObjectName("b_6")
        self.gridLayout_4.addWidget(self.b_6, 0, 9, 1, 1)
        self.b_8 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_8.setFont(font)
        self.b_8.setObjectName("b_8")
        self.gridLayout_4.addWidget(self.b_8, 0, 7, 1, 1)
        self.b_9 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_9.setFont(font)
        self.b_9.setObjectName("b_9")
        self.gridLayout_4.addWidget(self.b_9, 0, 6, 1, 1)
        self.b_s = QtWidgets.QPushButton(self.frame_3)
        self.b_s.setText("")
        self.b_s.setObjectName("b_s")
        self.gridLayout_4.addWidget(self.b_s, 4, 7, 1, 5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 3, 0, 1, 7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 3, 12, 1, 4)
        self.b_26 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_26.setFont(font)
        self.b_26.setObjectName("b_26")
        self.gridLayout_4.addWidget(self.b_26, 2, 11, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 2, 0, 1, 4)
        self.b_27 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_27.setFont(font)
        self.b_27.setObjectName("b_27")
        self.gridLayout_4.addWidget(self.b_27, 2, 10, 1, 1)
        self.b_32 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_32.setFont(font)
        self.b_32.setObjectName("b_32")
        self.gridLayout_4.addWidget(self.b_32, 2, 5, 1, 1)
        self.b_29 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_29.setFont(font)
        self.b_29.setObjectName("b_29")
        self.gridLayout_4.addWidget(self.b_29, 2, 8, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 2, 13, 1, 3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 1, 0, 1, 3)
        self.b_13 = QtWidgets.QToolButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_13.setFont(font)
        self.b_13.setObjectName("b_13")
        self.gridLayout_4.addWidget(self.b_13, 0, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem10, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.gridLayout_3.addWidget(self.frame_5, 1, 0, 1, 4)
        self.txte_affichage = QtWidgets.QTextEdit(self.split_frame)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.txte_affichage.setFont(font)
        self.txte_affichage.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txte_affichage.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txte_affichage.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txte_affichage.setObjectName("txte_affichage")
        self.gridLayout_3.addWidget(self.txte_affichage, 0, 0, 1, 4)
        self.verticalLayout.addWidget(self.split_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Splited"))
        self.btn_open.setText(_translate("MainWindow", "Open"))
        self.tb_save_folder.setText(_translate("MainWindow", "Save at"))
        self.btn_avance.setText(_translate("MainWindow", "A"))
        self.btn_recal_plus.setText(_translate("MainWindow", "R+"))
        self.btn_avance_plus.setText(_translate("MainWindow", "A+"))
        self.pb_play_subsound.setText(_translate("MainWindow", "Play sub audio"))
        self.btn_recal.setText(_translate("MainWindow", "R"))
        self.pb_define_start.setText(_translate("MainWindow", "Start At"))
        self.te_start_subsound.setDisplayFormat(_translate("MainWindow", "mm:ss:z"))
        self.te_end_subsound.setDisplayFormat(_translate("MainWindow", "mm:ss:z"))
        self.pb_translate_sound.setText(_translate("MainWindow", "Translate"))
        self.pb_define_end.setText(_translate("MainWindow", "End At"))
        self.pb_save.setText(_translate("MainWindow", "Add"))
        self.b_10.setText(_translate("MainWindow", "ث"))
        self.b_5.setText(_translate("MainWindow", "ه"))
        self.b_11.setText(_translate("MainWindow", "ص"))
        self.b_7.setText(_translate("MainWindow", "غ"))
        self.b_12.setText(_translate("MainWindow", "ض"))
        self.b_del.setText(_translate("MainWindow", "Del"))
        self.b_1.setText(_translate("MainWindow", "د"))
        self.b_31.setText(_translate("MainWindow", "ؤ"))
        self.b_3.setText(_translate("MainWindow", "ح"))
        self.b_4.setText(_translate("MainWindow", "خ"))
        self.b_16.setText(_translate("MainWindow", "م"))
        self.b_14.setText(_translate("MainWindow", "ط"))
        self.b_25.setText(_translate("MainWindow", "ظ"))
        self.b_17.setText(_translate("MainWindow", "ن"))
        self.b_2.setText(_translate("MainWindow", "ج"))
        self.b_15.setText(_translate("MainWindow", "ك"))
        self.b_19.setText(_translate("MainWindow", "ا"))
        self.b_21.setText(_translate("MainWindow", "ب"))
        self.b_18.setText(_translate("MainWindow", "ت"))
        self.b_20.setText(_translate("MainWindow", "ل"))
        self.b_22.setText(_translate("MainWindow", "ي"))
        self.b_34.setText(_translate("MainWindow", "أ"))
        self.b_23.setText(_translate("MainWindow", "س"))
        self.b_24.setText(_translate("MainWindow", "ش"))
        self.b_30.setText(_translate("MainWindow", "ر"))
        self.b_35.setText(_translate("MainWindow", "إ"))
        self.b_37.setText(_translate("MainWindow", "لا"))
        self.b_33.setText(_translate("MainWindow", "ئ"))
        self.b_38.setText(_translate("MainWindow", "آ"))
        self.b_36.setText(_translate("MainWindow", "لإ"))
        self.b_28.setText(_translate("MainWindow", "ة"))
        self.b_6.setText(_translate("MainWindow", "ع"))
        self.b_8.setText(_translate("MainWindow", "ف"))
        self.b_9.setText(_translate("MainWindow", "ق"))
        self.b_26.setText(_translate("MainWindow", "ز"))
        self.b_27.setText(_translate("MainWindow", "و"))
        self.b_32.setText(_translate("MainWindow", "ء"))
        self.b_29.setText(_translate("MainWindow", "ى"))
        self.b_13.setText(_translate("MainWindow", "ذ"))
        self.txte_affichage.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
