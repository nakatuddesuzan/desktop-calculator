import sys

from PyQt5.QtWidgets import QApplication
from view import PyCalc
from model import evaluateExpression
from controller import PyCalcCtrl


def main():
    app = QApplication(sys.argv)
    view = PyCalc()
    view.show()
    model = evaluateExpression
    PyCalcCtrl(model=model, view=view)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()