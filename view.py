from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow,
                             QWidget,
                             QVBoxLayout,
                             QLineEdit,
                             QGridLayout,
                             QPushButton,
                             )


class PyCalc(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setWindowIconText("PyCalc")
        self.setFixedSize(400, 400)
        self.generalLayout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.generalLayout)
        self.createDisplay()
        self.createButtons()
    
    def createDisplay(self):
        self.display = QLineEdit()
        # set display size
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # add display to general Layout
        self.generalLayout.addWidget(self.display)
    
    def createButtons(self):
        self.btns = {}
        btnsLayout = QGridLayout()
        btns = {'7': (0,0),
                '8': (0,1),
                '9': (0,2),
                'C': (0,3),
                '4': (1,0),
                '5': (1,1),
                '6': (1,2),
                '*': (1,3),
                '3': (2,0),
                '2': (2,1),
                '1': (2,2),
                '-': (2,3),
                '0': (3,0),
                '.': (3,1),
                '=': (3,2),
                '+': (3,3),
               }
        for button, buttonPos in btns.items():
            self.btns[button] = QPushButton(button)
            self.btns[button].setFixedSize(80, 80)
            btnsLayout.addWidget(self.btns[button], buttonPos[0], buttonPos[1])
        # add btns layout to the general layout
        self.generalLayout.addLayout(btnsLayout)
        
    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText('')    
    

