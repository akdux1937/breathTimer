# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(393, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerFrame = QtWidgets.QFrame(self.centralwidget)
        self.headerFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.headerFrame.setLineWidth(0)
        self.headerFrame.setObjectName("headerFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.headerFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headerLabel = QtWidgets.QLabel(self.headerFrame)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.headerLabel.setFont(font)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_2.addWidget(self.headerLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addWidget(self.headerFrame, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.centerFrame = QtWidgets.QFrame(self.centralwidget)
        self.centerFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.centerFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.centerFrame.setLineWidth(0)
        self.centerFrame.setObjectName("centerFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centerFrame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.centerFrame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_4.setLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(12, 0, 12, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.helpLabel = QtWidgets.QLabel(self.frame_4)
        self.helpLabel.setObjectName("helpLabel")
        self.verticalLayout_4.addWidget(self.helpLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.progressBar = QtWidgets.QProgressBar(self.frame_4)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.lcd = QtWidgets.QLCDNumber(self.frame_4)
        self.lcd.setMinimumSize(QtCore.QSize(0, 60))
        self.lcd.setObjectName("lcd")
        self.verticalLayout_4.addWidget(self.lcd)
        self.startBtn = QtWidgets.QPushButton(self.frame_4)
        self.startBtn.setObjectName("startBtn")
        self.verticalLayout_4.addWidget(self.startBtn)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.centerFrame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_5.setLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelBtn = QtWidgets.QPushButton(self.frame_5)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.saveBtn = QtWidgets.QPushButton(self.frame_5)
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout.addWidget(self.saveBtn)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.centerFrame)
        self.tableFrame = QtWidgets.QFrame(self.centralwidget)
        self.tableFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tableFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableFrame.setLineWidth(0)
        self.tableFrame.setObjectName("tableFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tableFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableView = QtWidgets.QTableView(self.tableFrame)
        self.tableView.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tableView.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableView.setLineWidth(0)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout_2.addWidget(self.tableView)
        self.verticalLayout.addWidget(self.tableFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headerLabel.setText(_translate("MainWindow", "Breath Timer"))
        self.helpLabel.setText(_translate("MainWindow", "TextLabel"))
        self.startBtn.setText(_translate("MainWindow", "Start / Stop"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel / Reset"))
        self.saveBtn.setText(_translate("MainWindow", "Save"))