# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'album.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1680, 1050)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(1390, 180, 241, 31))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(19)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(76, 76, 76, 50))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.listWidget_2.addItem(item)
        self.listWidget_5 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_5.setGeometry(QtCore.QRect(1390, 220, 241, 31))
        self.listWidget_5.setObjectName("listWidget_5")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(19)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(76, 76, 76, 50))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.listWidget_5.addItem(item)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-40, -20, 1711, 1031))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.uploadvideo = QtWidgets.QWidget()
        self.uploadvideo.setObjectName("uploadvideo")
        self.uploadbuttom = QtWidgets.QPushButton(self.uploadvideo)
        self.uploadbuttom.setGeometry(QtCore.QRect(440, 430, 471, 71))
        self.uploadbuttom.setMinimumSize(QtCore.QSize(401, 52))
        font = QtGui.QFont()
        font.setFamily("Kannada MN")
        font.setPointSize(24)
        self.uploadbuttom.setFont(font)
        self.uploadbuttom.setAutoFillBackground(False)
        self.uploadbuttom.setStyleSheet("QPushButton{\n"
"   border-radius: 20px;  border: 3px groove gray;\n"
" \n"
"}\n"
"")
        self.uploadbuttom.setCheckable(True)
        self.uploadbuttom.setObjectName("uploadbuttom")
        self.stackedWidget.addWidget(self.uploadvideo)
        self.viewalbums = QtWidgets.QWidget()
        self.viewalbums.setObjectName("viewalbums")
        self.label_2 = QtWidgets.QLabel(self.viewalbums)
        self.label_2.setGeometry(QtCore.QRect(460, 160, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.scrollArea = QtWidgets.QScrollArea(self.viewalbums)
        self.scrollArea.setGeometry(QtCore.QRect(460, 250, 931, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 929, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 921, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.verticalLayout_5.addWidget(self.label_31)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 3, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.gridLayout.addLayout(self.verticalLayout_7, 0, 1, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_8.addWidget(self.label_13)
        self.gridLayout.addLayout(self.verticalLayout_8, 0, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.viewalbums)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(280, 160, 160, 841))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.viewalbums)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(210, 160, 61, 841))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.viewalbums)
        self.label_5.setGeometry(QtCore.QRect(110, 160, 81, 20))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.viewalbums)
        self.label_7.setGeometry(QtCore.QRect(90, 40, 171, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_7.setObjectName("label_7")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.viewalbums)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(280, 80, 361, 32))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_4.addWidget(self.comboBox, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 1, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.gridLayoutWidget_4)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_4.addWidget(self.dateTimeEdit, 0, 2, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.viewalbums)
        self.tabWidget.setGeometry(QtCore.QRect(460, 670, 931, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(590, 20, 62, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_2.addWidget(self.label_18)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(660, 20, 251, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout.addWidget(self.pushButton_10)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 0, 561, 291))
        self.label.setObjectName("label")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab)
        self.pushButton_16.setGeometry(QtCore.QRect(470, 270, 113, 32))
        self.pushButton_16.setObjectName("pushButton_16")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(660, 20, 251, 281))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_4.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(10, 0, 561, 291))
        self.label_12.setObjectName("label_12")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(590, 20, 62, 281))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_3.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_3.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_3.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_3.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_3.addWidget(self.label_23)
        self.tabWidget.addTab(self.tab_2, "")
        self.label_6 = QtWidgets.QLabel(self.viewalbums)
        self.label_6.setGeometry(QtCore.QRect(120, 980, 81, 20))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_11 = QtWidgets.QPushButton(self.viewalbums)
        self.pushButton_11.setGeometry(QtCore.QRect(660, 80, 113, 32))
        self.pushButton_11.setObjectName("pushButton_11")
        self.comboBox_2 = QtWidgets.QComboBox(self.viewalbums)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 460, 71, 32))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(self.viewalbums)
        self.label_3.setGeometry(QtCore.QRect(140, 460, 60, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.viewalbums)
        self.label_4.setGeometry(QtCore.QRect(80, 430, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_12 = QtWidgets.QPushButton(self.viewalbums)
        self.pushButton_12.setGeometry(QtCore.QRect(70, 560, 131, 32))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.viewalbums)
        self.pushButton_13.setGeometry(QtCore.QRect(70, 590, 131, 32))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.viewalbums)
        self.pushButton_14.setGeometry(QtCore.QRect(200, 150, 81, 71))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"    border-radius: 20px;  border: 10px groove gray;\n"
"}")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.viewalbums)
        self.pushButton_15.setGeometry(QtCore.QRect(100, 620, 71, 32))
        self.pushButton_15.setObjectName("pushButton_15")
        self.frame = QtWidgets.QFrame(self.viewalbums)
        self.frame.setGeometry(QtCore.QRect(210, 160, 61, 841))
        self.frame.setStyleSheet("QFrame{\n"
"  border: 3px groove gray;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.viewalbums)
        self.frame_2.setGeometry(QtCore.QRect(280, 160, 161, 841))
        self.frame_2.setStyleSheet("QFrame{\n"
" border: 3px groove gray;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.viewalbums)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(100, 530, 71, 31))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 0, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.viewalbums)
        self.label_24.setGeometry(QtCore.QRect(1230, 210, 179, 29))
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.viewalbums)
        self.label_25.setGeometry(QtCore.QRect(1030, 210, 179, 29))
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.label_28 = QtWidgets.QLabel(self.viewalbums)
        self.label_28.setGeometry(QtCore.QRect(840, 210, 179, 29))
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.viewalbums)
        self.label_29.setGeometry(QtCore.QRect(650, 210, 179, 29))
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.viewalbums)
        self.label_30.setGeometry(QtCore.QRect(460, 210, 179, 29))
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.frame.raise_()
        self.frame_2.raise_()
        self.tabWidget.raise_()
        self.label_2.raise_()
        self.scrollArea.raise_()
        self.gridLayoutWidget_2.raise_()
        self.gridLayoutWidget_3.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.gridLayoutWidget_4.raise_()
        self.label_6.raise_()
        self.pushButton_11.raise_()
        self.comboBox_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.pushButton_15.raise_()
        self.gridLayoutWidget_5.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_28.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.stackedWidget.addWidget(self.viewalbums)
        self.viewlabels = QtWidgets.QWidget()
        self.viewlabels.setObjectName("viewlabels")
        self.stackedWidget.addWidget(self.viewlabels)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(1370, 30, 281, 951))
        self.listView.setObjectName("listView")
        self.touxiang = QtWidgets.QPushButton(self.centralwidget)
        self.touxiang.setEnabled(True)
        self.touxiang.setGeometry(QtCore.QRect(1480, 90, 61, 61))
        self.touxiang.setStyleSheet("QPushButton{\n"
"    border-image: url(:/新前缀/默认头像-灰.jpg);\n"
"    \n"
"   \n"
"     border-radius: 30px;  border: 2px groove gray;\n"
"    \n"
"}")
        self.touxiang.setText("")
        self.touxiang.setObjectName("touxiang")
        self.listWidget_6 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_6.setGeometry(QtCore.QRect(1390, 260, 241, 31))
        self.listWidget_6.setObjectName("listWidget_6")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(19)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(76, 76, 76, 50))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.listWidget_6.addItem(item)
        self.listWidget_7 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_7.setGeometry(QtCore.QRect(1390, 300, 241, 31))
        self.listWidget_7.setObjectName("listWidget_7")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(19)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(76, 76, 76, 50))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.listWidget_7.addItem(item)
        self.stackedWidget.raise_()
        self.listView.raise_()
        self.listWidget_2.raise_()
        self.listWidget_5.raise_()
        self.touxiang.raise_()
        self.listWidget_6.raise_()
        self.listWidget_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1680, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "Upload video"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)
        item = self.listWidget_5.item(0)
        item.setText(_translate("MainWindow", "View existed videos"))
        self.listWidget_5.setSortingEnabled(__sortingEnabled)
        self.uploadbuttom.setText(_translate("MainWindow", "Upload video from this device"))
        self.label_2.setText(_translate("MainWindow", "Labels"))
        self.label_7.setText(_translate("MainWindow", "DAY"))
        self.comboBox.setItemText(0, _translate("MainWindow", "DAY"))
        self.comboBox.setItemText(1, _translate("MainWindow", "WEEK"))
        self.comboBox.setItemText(2, _translate("MainWindow", "MONTH"))
        self.comboBox.setItemText(3, _translate("MainWindow", "YEAR"))
        self.label_8.setText(_translate("MainWindow", "              FROM:"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "No image is selected"))
        self.pushButton_16.setText(_translate("MainWindow", "next image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "original image"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label_12.setText(_translate("MainWindow", "No image is selected"))
        self.label_19.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "TextLabel"))
        self.label_21.setText(_translate("MainWindow", "TextLabel"))
        self.label_22.setText(_translate("MainWindow", "TextLabel"))
        self.label_23.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "feature heatmap"))
        self.pushButton_11.setText(_translate("MainWindow", "OK"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1/12"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1/8"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "1/4"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "1/2"))
        self.label_3.setText(_translate("MainWindow", "DAY"))
        self.label_4.setText(_translate("MainWindow", "ZOOM SCALE"))
        self.pushButton_12.setText(_translate("MainWindow", "Next scale"))
        self.pushButton_13.setText(_translate("MainWindow", "Last scale"))
        self.pushButton_15.setText(_translate("MainWindow", "SHOW"))
        self.label_26.setText(_translate("MainWindow", " /"))
        self.label_27.setText(_translate("MainWindow", "12"))
        self.label_9.setText(_translate("MainWindow", "1"))
        __sortingEnabled = self.listWidget_6.isSortingEnabled()
        self.listWidget_6.setSortingEnabled(False)
        item = self.listWidget_6.item(0)
        item.setText(_translate("MainWindow", "View place albums"))
        self.listWidget_6.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_7.isSortingEnabled()
        self.listWidget_7.setSortingEnabled(False)
        item = self.listWidget_7.item(0)
        item.setText(_translate("MainWindow", "Manage labels"))
        self.listWidget_7.setSortingEnabled(__sortingEnabled)
