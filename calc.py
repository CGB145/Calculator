import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QGridLayout, QHBoxLayout, QSizePolicy,QVBoxLayout, QLineEdit, QWidget, QTextEdit
from PyQt5.QtCore import QSize
import qdarktheme

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.line = QLineEdit("Yo")
        self.text = QTextEdit()
        self.text.setMinimumWidth(100)
        self.text.setMaximumWidth(300)
        
        self.button1 = QPushButton('1')        
        self.button1.setMinimumHeight(50)
        self.button1.setMinimumWidth(50)
        self.button2 = QPushButton('2')        
        self.button2.setMinimumHeight(50)
        self.button2.setMinimumWidth(50)
        self.button3 = QPushButton('3')        
        self.button3.setMinimumHeight(50)
        self.button3.setMinimumWidth(50)
        self.button4 = QPushButton('4')        
        self.button4.setMinimumHeight(50)
        self.button4.setMinimumWidth(50)
        self.button5 = QPushButton('5')        
        self.button5.setMinimumHeight(50)
        self.button5.setMinimumWidth(50)
        self.button6 = QPushButton('6')        
        self.button6.setMinimumHeight(50)
        self.button6.setMinimumWidth(50)
        self.button7 = QPushButton('7')        
        self.button7.setMinimumHeight(50)
        self.button7.setMinimumWidth(50)
        self.button8 = QPushButton('8')        
        self.button8.setMinimumHeight(50)
        self.button8.setMinimumWidth(50)
        self.button9 = QPushButton('9')        
        self.button9.setMinimumHeight(50)
        self.button9.setMinimumWidth(50)


        self.pLayout = QVBoxLayout(self)
        self.hLayout = QHBoxLayout(self)
        self.cLayout = QGridLayout(self)
        self.pLayout.addWidget(self.line)
        self.pLayout.addLayout(self.hLayout)
        self.hLayout.addWidget(self.text)
        self.hLayout.addLayout(self.cLayout)



        policy = QSizePolicy.Policy.Expanding
        for i in range(1,10):
            exec(f"self.button{i}.setSizePolicy(policy,policy)")


        self.cLayout.addWidget(self.button1,0,0)
        self.cLayout.addWidget(self.button2,0,1)
        self.cLayout.addWidget(self.button3,0,2)
        self.cLayout.addWidget(self.button4,1,0)
        self.cLayout.addWidget(self.button5,1,1)
        self.cLayout.addWidget(self.button6,1,2)
        self.cLayout.addWidget(self.button7,2,0)
        self.cLayout.addWidget(self.button8,2,1)
        self.cLayout.addWidget(self.button9,2,2)





            

        
        
        
if __name__ == "__main__":
    app = QApplication([])
    qdarktheme.setup_theme()
    widget = MyWidget()
    widget.style
    widget.resize(350, 350)
    widget.setWindowTitle("Calculator")
    widget.show()


    sys.exit(app.exec())