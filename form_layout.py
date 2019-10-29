import sys


#QVBoxLayout arranges widgets vertically from top to bottom
from PyQt5.QtWidgets import (QApplication, 
                             QFormLayout, 
                             QPushButton, 
                             QLineEdit, 
                             QWidget,
                             QDialog,
                             QVBoxLayout,
                             QDialogButtonBox,
                             )

class Dialog(QDialog):
    """ Dialog """
    
    def __init__(self, parent=None):
        """ Initializer"""
        super().__init__(parent)
        self.setWindowTitle("Sign In")
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()

        formLayout.addRow("Name:", QLineEdit())
        formLayout.addRow("Age:", QLineEdit())
        formLayout.addRow("Fun Fact:", QLineEdit())
        formLayout.addRow("Sex:", QLineEdit())
        
        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
