from functools import partial
from model import ERROR_MSG
 
class PyCalcCtrl():
    
    
    def __init__(self, model, view):
        self.evaluate = model
        self.view = view
        self.connectSignals()
        
    def calculateResult(self):
        result = self.evaluate(expression=self.view.displayText())
        self.view.setDisplayText(result)
    
    def buildExpression(self, sub_exp):
        if self.view.displayText() == ERROR_MSG:
            self.view.clearDisplay()
        expression = self.view.displayText() + sub_exp
        self.view.setDisplayText(expression)
    
    def connectSignals(self):
        """Connect signals and slots."""
        for button, buttonPos in self.view.btns.items():
            if button not in {'=', 'C'}:
                buttonPos.clicked.connect(partial(self.buildExpression, button))

        self.view.btns['='].clicked.connect(self.calculateResult)
        self.view.display.returnPressed.connect(self.calculateResult)
        self.view.btns['C'].clicked.connect(self.view.clearDisplay)
