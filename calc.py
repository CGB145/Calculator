#!/usr/bin/python

import sys
import re
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QGridLayout, QHBoxLayout, QSizePolicy,QVBoxLayout, QLineEdit, QWidget, QTextEdit
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
import qdarktheme

def findChar(string:str,char:str):
    allChars = []
    for x in string:
        if x == char:
            allChars.append(x)
    return allChars
    



class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        font = QFont()
        font.setPointSize(20)


        self.line = QLineEdit("")
        self.line.setFont(font)
        self.text = QTextEdit()
        self.text.setFont(font)
        self.text.setMinimumWidth(100)
        self.text.setMaximumWidth(300)
        
        self.buttonC = QPushButton('C')        
        self.buttonC.setMinimumHeight(50)
        self.buttonC.setMinimumWidth(50)
        self.buttonC.setStyleSheet("color: red;")
        self.buttonC.setFont(font)
        self.buttonParanthese = QPushButton('()')        
        self.buttonParanthese.setMinimumHeight(50)
        self.buttonParanthese.setMinimumWidth(50)
        self.buttonParanthese.setStyleSheet("color: white;")
        self.buttonParanthese.setFont(font)
        self.buttonPercent = QPushButton('%')        
        self.buttonPercent.setMinimumHeight(50)
        self.buttonPercent.setMinimumWidth(50)
        self.buttonPercent.setStyleSheet("color: white;")
        self.buttonPercent.setFont(font)
        self.buttonForwardSlash = QPushButton('/')        
        self.buttonForwardSlash.setMinimumHeight(50)
        self.buttonForwardSlash.setMinimumWidth(50)
        self.buttonForwardSlash.setStyleSheet("color: white;")
        self.buttonForwardSlash.setFont(font)
        self.button7 = QPushButton('7')        
        self.button7.setMinimumHeight(50)
        self.button7.setMinimumWidth(50)
        self.button8 = QPushButton('8')        
        self.button8.setMinimumHeight(50)
        self.button8.setMinimumWidth(50)
        self.button9 = QPushButton('9')        
        self.button9.setMinimumHeight(50)
        self.button9.setMinimumWidth(50)
        self.buttonX = QPushButton('*')        
        self.buttonX.setMinimumHeight(50)
        self.buttonX.setMinimumWidth(50)
        self.buttonX.setStyleSheet("color: white;")
        self.buttonX.setFont(font)
        self.button4 = QPushButton('4')        
        self.button4.setMinimumHeight(50)
        self.button4.setMinimumWidth(50)
        self.button5 = QPushButton('5')        
        self.button5.setMinimumHeight(50)
        self.button5.setMinimumWidth(50)
        self.button6 = QPushButton('6')        
        self.button6.setMinimumHeight(50)
        self.button6.setMinimumWidth(50)
        self.buttonMinus = QPushButton('-')        
        self.buttonMinus.setMinimumHeight(50)
        self.buttonMinus.setMinimumWidth(50)
        self.buttonMinus.setStyleSheet("color: white;")
        self.buttonMinus.setFont(font)
        self.button1 = QPushButton('1')        
        self.button1.setMinimumHeight(50)
        self.button1.setMinimumWidth(50)
        self.button2 = QPushButton('2')        
        self.button2.setMinimumHeight(50)
        self.button2.setMinimumWidth(50)
        self.button3 = QPushButton('3')        
        self.button3.setMinimumHeight(50)
        self.button3.setMinimumWidth(50)
        self.buttonPlus = QPushButton('+')        
        self.buttonPlus.setMinimumHeight(50)
        self.buttonPlus.setMinimumWidth(50)
        self.buttonPlus.setStyleSheet("color: white;")
        self.buttonPlus.setFont(font)
        self.buttonPN = QPushButton('+/-')        
        self.buttonPN.setMinimumHeight(50)
        self.buttonPN.setMinimumWidth(50)
        self.buttonPN.setStyleSheet("color: white;")
        self.buttonPN.setFont(font)
        self.button0 = QPushButton('0')        
        self.button0.setMinimumHeight(50)
        self.button0.setMinimumWidth(50)
        self.buttonComa = QPushButton(',')        
        self.buttonComa.setMinimumHeight(50)
        self.buttonComa.setMinimumWidth(50)
        self.buttonComa.setStyleSheet("color: white;")
        self.buttonComa.setFont(font)
        self.buttonEquals = QPushButton('=')        
        self.buttonEquals.setMinimumHeight(50)
        self.buttonEquals.setMinimumWidth(50)
        self.buttonEquals.setMouseTracking(True)
        self.buttonEquals.setStyleSheet("background-color: green;")
        self.buttonEquals.setFont(font)



        


        self.pLayout = QVBoxLayout(self)
        self.hLayout = QHBoxLayout(self)
        self.cLayout = QGridLayout(self)
        self.pLayout.addWidget(self.line)
        self.pLayout.addLayout(self.hLayout)
        self.hLayout.addWidget(self.text)
        self.hLayout.addLayout(self.cLayout)



        policy = QSizePolicy.Policy.Expanding
        self.buttonC.setSizePolicy(policy,policy)
        self.buttonParanthese.setSizePolicy(policy,policy)
        self.buttonPercent.setSizePolicy(policy,policy)
        self.buttonForwardSlash.setSizePolicy(policy,policy)
        self.buttonX.setSizePolicy(policy,policy)
        self.buttonMinus.setSizePolicy(policy,policy)
        self.buttonPlus.setSizePolicy(policy,policy)
        self.buttonEquals.setSizePolicy(policy,policy)
        self.buttonComa.setSizePolicy(policy,policy)
        self.buttonPN.setSizePolicy(policy,policy)



        for i in range(10):
            exec(f"self.button{i}.setSizePolicy(policy,policy)")
            exec(f"self.button{i}.setFont(font)")


        self.cLayout.addWidget(self.buttonC,0,0)
        self.cLayout.addWidget(self.buttonParanthese,0,1)
        self.cLayout.addWidget(self.buttonPercent,0,2)
        self.cLayout.addWidget(self.buttonForwardSlash,0,3)
        self.cLayout.addWidget(self.button7,1,0)
        self.cLayout.addWidget(self.button8,1,1)
        self.cLayout.addWidget(self.button9,1,2)
        self.cLayout.addWidget(self.buttonX,1,3)
        self.cLayout.addWidget(self.button4,2,0)

        self.cLayout.addWidget(self.button5,2,1)
        self.cLayout.addWidget(self.button6,2,2)
        self.cLayout.addWidget(self.buttonMinus,2,3)
        self.cLayout.addWidget(self.button1,3,0)
        self.cLayout.addWidget(self.button2,3,1)
        self.cLayout.addWidget(self.button3,3,2)
        self.cLayout.addWidget(self.buttonPlus,3,3)
        self.cLayout.addWidget(self.buttonPN,4,0)
        self.cLayout.addWidget(self.button0,4,1)
        self.cLayout.addWidget(self.buttonComa,4,2)
        self.cLayout.addWidget(self.buttonEquals,4,3)

        self.button1.clicked.connect(self.getButtonText)
        self.button2.clicked.connect(self.getButtonText)
        self.button3.clicked.connect(self.getButtonText)
        self.button4.clicked.connect(self.getButtonText)
        self.button5.clicked.connect(self.getButtonText)
        self.button6.clicked.connect(self.getButtonText)
        self.button7.clicked.connect(self.getButtonText)
        self.button8.clicked.connect(self.getButtonText)
        self.button9.clicked.connect(self.getButtonText)
        self.buttonC.clicked.connect(self.clearLine)
        self.buttonParanthese.clicked.connect(self.insertParen)
        self.buttonPercent.clicked.connect(self.getButtonText)
        self.buttonForwardSlash.clicked.connect(self.getButtonText)
        self.buttonX.clicked.connect(self.getButtonText)
        self.buttonMinus.clicked.connect(self.getButtonText)
        self.buttonPlus.clicked.connect(self.getButtonText)
        self.buttonEquals.clicked.connect(self.calculate)
        self.buttonComa.clicked.connect(self.getButtonText)
        self.button0.clicked.connect(self.getButtonText)
        self.buttonPN.clicked.connect(self.setPN)



        self.clickedOnce=False





    #currently only working with one operation. Look at test.py for better re search
    def calculate(self):
        numbers = ["0","1","2","3","4","5","6","7","8","9","+","-","/","%","*","(",")",","]
        string = self.line.text()
        hasChars = False

        for i in string:
            if i in numbers:
                continue
            else:
                hasChars = True
                break



        
        string = string.replace("%","*0.1*")
        
        if  bool(string) and not hasChars:


            result = eval(string)

            self.line.setText(str(result))
            self.text.append(str(result))
        

    def setPN(self):
        self.line.insert("-")
    
    def clearLine(self):
        self.line.clear()
        self.clickedOnce = False

    def insertParen(self):
        parenthese = self.buttonParanthese.text()
        if self.clickedOnce == False:
            self.line.insert("(")
            self.clickedOnce = True
        elif self.clickedOnce == True:
            self.line.insert(")")
            self.clickedOnce = False

    def getButtonText(self):
        sender = app.sender()
        button = sender.text()
        self.line.insert(button)
 
if __name__ == "__main__":
    app = QApplication([])
    qdarktheme.setup_theme()
    widget = MyWidget()
    widget.style
    widget.resize(350, 350)
    widget.setWindowTitle("Calculator")
    widget.show()


    sys.exit(app.exec())