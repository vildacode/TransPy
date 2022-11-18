import os
from pathlib import Path
import sys
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtUiTools import *
from functools import partial
from subprocess import getstatusoutput
from ui_trans_py import Ui_Form as ui



class Widget(QWidget,ui):
    def __init__(self):
        super(Widget, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("TransPy")
        self.setWindowIcon(QtGui.QIcon("Data/PNG/Untitled-1.png"))

        #Process terminal live shell
        self.process=QtCore.QProcess(self)
        self.process.setProgram("python")
        self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)

        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self.process.finished.connect(self.on_finished)

        #Item window terminal
        self.Terminal = self.findChild(QTextEdit, "Terminal")

        #Line enter name file
        self.Enter_name = self.findChild(QLineEdit,"Enter_name")

        #Item select file python
        self.Button_Py = self.findChild(QPushButton, "Button_Py").clicked.connect(lambda: self.OpenFiles("Button_Py"))
        self.SelectPy = self.findChild(QLineEdit, "SelectPy")

        #Item select Icon for file exe
        self.Button_Ico = self.findChild(QPushButton, "Button_Ico").clicked.connect(lambda: self.OpenFiles("Button_Ico"))
        self.SelectIco = self.findChild(QLineEdit, "SelectIco")

        #Item select folder save file exe
        self.Button_save = self.findChild(QPushButton, "Button_save").clicked.connect(lambda: self.OpenFiles("Button_save"))
        self.SaveFile = self.findChild(QLineEdit, "SaveFile")

        #Item button radio for one file
        self.radio_OneFile = self.findChild(QRadioButton, "radio_OneFile").isChecked()

        self.Administrator = self.findChild(QPushButton,"Administrator")
        self.Remove_Console = self.findChild(QPushButton,"Remove_Console")

        #Finsh button
        self.Button_Finsh = self.findChild(QPushButton, "Button_Finsh")
        self.Button_Finsh.clicked.connect(lambda: self.Finsh())

    # def load_ui(self):
    #     loader = QUiLoader()
    #     path = os.fspath(Path(__file__).resolve().parent / "trans_py.ui")
    #     ui_file = QFile(path)
    #     ui_file.open(QFile.ReadOnly)
    #     loader.load(ui_file, self)
    #     ui_file.close()

    def OpenFiles(self,key):
        #Select file python
        if key == "Button_Py":
            self.FilePy = QFileDialog.getOpenFileName(self, "Select file python", "", "Python file (*.py)")
            self.SelectPy.setText(str(self.FilePy[0]))
        #Select Icon for file exe
        elif key == "Button_Ico":
            self.FileIco = QFileDialog.getOpenFileName(self, "Select Icon", "", "Icon file (*.ico);;png file (*.png);;jpg file (*.jpg)")
            self.SelectIco.setText(str(self.FileIco[0]))
        #Select folder save file exe
        elif key == "Button_save":
            self.File_Save = QFileDialog.getExistingDirectory(self, "Select Icon")
            self.SaveFile.setText(str(self.File_Save))

    def Finsh(self):

        #kill command line
        if self.Button_Finsh.text() == "Stop":
            self.process.kill()

        #Error select file python
        if self.SelectPy.text() == "":
            self.TerminalColors("Error: Please Select file python","#FC025B")
            pass
        else:
            self.Command = ["PyInstallers"]

            #Administrator
            if self.Administrator.isChecked() == True:
                self.Command.append("--uac-admin")

            #Remove console window
            if self.Remove_Console.isChecked() == True:
                self.Command.append("-w")

            #One file or files 
            if self.radio_OneFile == True: #One file
                self.Command.append("--onefile")
            else: #Files
                self.Command.append("-D")

            #Add icon to file exe
            if self.SelectIco != "":
                self.Command.append("-i")
                self.Command.append(self.SelectIco.text())

            #Folder save file exe
            if self.SaveFile.text() != "":
                self.Command.append('--distpath') 
                self.Command.append(self.SaveFile.text())
                
            #Enter name for file exe
            if self.Enter_name.text() != "":
                self.Command.append("-n")
                self.Command.append(self.Enter_name.text())

            self.Command.append(self.SelectPy.text())

            self.process.setArguments(self.Command)
            self.process.start()
            self.Button_Finsh.setText("Stop")
            self.Button_Finsh.setStyleSheet("background-color: rgb(158, 158, 158);")

    def on_readyReadStandardOutput(self):
        text = self.process.readAllStandardOutput().data().decode()
        self.Terminal.append(text)
    def on_finished(self):
        self.TerminalColors("=========================\nFile conversion succeeded\n=========================","#50D890")
        self.Button_Finsh.setText("Finsh")
        self.Button_Finsh.setStyleSheet("background-color:rgb(80, 216, 144);")

    #Colors text terminal
    def TerminalColors(self,text,color):
        TextColors = f"<span style=\" color: {color};\">{text}</span>"
        self.Terminal.append(TextColors)

if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
