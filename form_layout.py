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
                             QComboBox,
                             )

class Dialog(QDialog):
    """ Dialog """
    
    def __init__(self, parent=None):
        """ Initializer"""
        super().__init__(parent)
        self.setWindowTitle("Sign In")
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        
        self.cb = QComboBox()
        self.cb.addItems(["English", "Luganda", "Kiswahili", "French", "Spanish"])
        self.cb.currentIndexChanged.connect(self.selectionChange)
        formLayout.addWidget(self.cb)

        formLayout.addRow("Name:", QLineEdit())
        formLayout.addRow("Age:", QLineEdit())
        formLayout.addRow("Fun Fact:", QLineEdit())
        formLayout.addRow("Sex:", QLineEdit())
        formLayout.addRow("Language:", self.cb)
    
        
        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)
        
    def selectionChange(self, i):
        print("Items in the list are :")
        for count in range(self.cb.count()):
            print (self.cb.itemText(count))
        print ("Current index",i,"selection changed ",self.cb.currentText())
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
