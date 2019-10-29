import sys


#QHBoxLayout arranges widgets horizontally from left to right
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QWidget)


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Programming Languages")
layout = QHBoxLayout()

layout.addWidget(QPushButton('Python'))
layout.addWidget(QPushButton('Javascript'))
layout.addWidget(QPushButton('Java'))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
