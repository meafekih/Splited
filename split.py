# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:/Splited/Splited/split.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Split(object):
    def setupUi(self, Split):
        Split.setObjectName("Split")
        Split.resize(359, 477)
        self.verticalLayout = QtWidgets.QVBoxLayout(Split)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Split)
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
        self.frame = QtWidgets.QFrame(Split)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_recal_plus = QtWidgets.QToolButton(self.frame)
        self.btn_recal_plus.setObjectName("btn_recal_plus")
        self.gridLayout_2.addWidget(self.btn_recal_plus, 3, 0, 1, 1)
        self.btn_avance = QtWidgets.QToolButton(self.frame)
        self.btn_avance.setObjectName("btn_avance")
        self.gridLayout_2.addWidget(self.btn_avance, 3, 3, 1, 1)
        self.btn_avance_plus = QtWidgets.QToolButton(self.frame)
        self.btn_avance_plus.setObjectName("btn_avance_plus")
        self.gridLayout_2.addWidget(self.btn_avance_plus, 3, 4, 1, 1)
        self.lbl_duration = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_duration.setFont(font)
        self.lbl_duration.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbl_duration.setText("")
        self.lbl_duration.setObjectName("lbl_duration")
        self.gridLayout_2.addWidget(self.lbl_duration, 3, 5, 1, 1)
        self.slider = QtWidgets.QSlider(self.frame)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.gridLayout_2.addWidget(self.slider, 0, 0, 1, 6)
        self.ds_chorono = QtWidgets.QDoubleSpinBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ds_chorono.setFont(font)
        self.ds_chorono.setDecimals(3)
        self.ds_chorono.setMaximum(3600.0)
        self.ds_chorono.setSingleStep(0.1)
        self.ds_chorono.setObjectName("ds_chorono")
        self.gridLayout_2.addWidget(self.ds_chorono, 3, 2, 1, 1)
        self.btn_recal = QtWidgets.QToolButton(self.frame)
        self.btn_recal.setObjectName("btn_recal")
        self.gridLayout_2.addWidget(self.btn_recal, 3, 1, 1, 1)
        self.pb_play_subsound = QtWidgets.QPushButton(self.frame)
        self.pb_play_subsound.setObjectName("pb_play_subsound")
        self.gridLayout_2.addWidget(self.pb_play_subsound, 7, 0, 1, 3)
        self.pb_translate_sound = QtWidgets.QPushButton(self.frame)
        self.pb_translate_sound.setObjectName("pb_translate_sound")
        self.gridLayout_2.addWidget(self.pb_translate_sound, 7, 3, 1, 3)
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
        self.pb_define_start = QtWidgets.QPushButton(self.frame)
        self.pb_define_start.setObjectName("pb_define_start")
        self.gridLayout_2.addWidget(self.pb_define_start, 5, 0, 1, 3)
        self.pb_define_end = QtWidgets.QPushButton(self.frame)
        self.pb_define_end.setObjectName("pb_define_end")
        self.gridLayout_2.addWidget(self.pb_define_end, 6, 0, 1, 3)
        self.verticalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(Split)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(3)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pb_save = QtWidgets.QPushButton(self.frame_3)
        self.pb_save.setObjectName("pb_save")
        self.gridLayout_3.addWidget(self.pb_save, 1, 3, 1, 1)
        self.txte_affichage = QtWidgets.QTextEdit(self.frame_3)
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
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(Split)
        QtCore.QMetaObject.connectSlotsByName(Split)

    def retranslateUi(self, Split):
        _translate = QtCore.QCoreApplication.translate
        Split.setWindowTitle(_translate("Split", "Split"))
        self.btn_open.setText(_translate("Split", "Open"))
        self.tb_save_folder.setText(_translate("Split", "Save at"))
        self.btn_recal_plus.setText(_translate("Split", "R+"))
        self.btn_avance.setText(_translate("Split", "A"))
        self.btn_avance_plus.setText(_translate("Split", "A+"))
        self.btn_recal.setText(_translate("Split", "R"))
        self.pb_play_subsound.setText(_translate("Split", "Play sub audio"))
        self.pb_translate_sound.setText(_translate("Split", "Translate"))
        self.te_start_subsound.setDisplayFormat(_translate("Split", "mm:ss:z"))
        self.te_end_subsound.setDisplayFormat(_translate("Split", "mm:ss:z"))
        self.pb_define_start.setText(_translate("Split", "Start At"))
        self.pb_define_end.setText(_translate("Split", "End At"))
        self.pb_save.setText(_translate("Split", "Add"))
        self.txte_affichage.setHtml(_translate("Split", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Split = QtWidgets.QWidget()
    ui = Ui_Split()
    ui.setupUi(Split)
    Split.show()
    sys.exit(app.exec_())
