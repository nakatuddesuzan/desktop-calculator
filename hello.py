#help to handle the exit status of the application
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

#create an instance of the QApplication
app = QApplication(sys.argv)

#create an instance of the application's GUI

window = QWidget()
window.setWindowTitle('hello app')
#determine the size of the window
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel("<h1>Hello Suzan!</h1>", parent=window)
helloMsg.move(60,15)

#show your application's GUI
window.show()

# Run your application's event loop (or main loop)
sys.exit(app.exec_())
