import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Budget Tracker")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.setWindowIcon(QtGui.QIcon('money.png'))

        self.statusBar()
    
        self.home()

    def home(self):
        earnings_label = QtGui.QLabel('Earnings: ', self)
        earnings_label.move(10,5)
        
        self.earningsTextbox = QtGui.QLineEdit(self)
        self.earningsTextbox.move(100, 5)
        self.earningsTextbox.resize(100, 25)
        
        percent_to_save_label = QtGui.QLabel('% to save: ', self)
        percent_to_save_label.move(10, 40)                                   

        self.percentTextbox = QtGui.QLineEdit(self)
        self.percentTextbox.move(100, 40)
        self.percentTextbox.resize(100, 25)

        budget_label = QtGui.QLabel('Budget: ', self)
        budget_label.move(125, 125)
        amount_saved = QtGui.QLabel('Amount saved: ', self)
        amount_saved.move(125, 160)

        self.budgetTextbox = QtGui.QLineEdit(self)
        self.budgetTextbox.move(215, 125)
        self.budgetTextbox.resize(100, 25)
        self.amountSavedTextbox = QtGui.QLineEdit(self)
        self.amountSavedTextbox.move(215, 160)
        self.amountSavedTextbox.resize(100, 25)

        calculate_btn = QtGui.QPushButton("Calculate", self)
        calculate_btn.clicked.connect(self.calculate_btn_on_click)
        calculate_btn.resize(75, 50)
        calculate_btn.move(10, 125)

       
                                         
        self.show()
 
    def calculate_btn_on_click(self):
        
        earnings =  self.earningsTextbox.text()
        percent = self.percentTextbox.text()

        self.statusBar().showMessage('You made '+str(earnings)+' dollars and would like to save '+str(percent)+'%')

        percent = float(percent) * 0.01
        budget = float(earnings) - float(earnings) * percent
        savings = float(earnings) - budget

        self.budgetTextbox.setText(str(budget))
        self.amountSavedTextbox.setText(str(savings))


    def computeBudget(earnings, percent_to_save):
        message = "You made "+str(earnings)+" dollars, and want to save "+str(percent_to_save)+"% of those earnings\n"
        
        percent_to_save = percent_to_save * 0.01
        budget = earnings - earnings * percent_to_save
        savings = earnings - budget

        message += "You have "+str(budget)+" dollars left in your budget to spend.\n"
        message += "You have saved "+str(savings)+" dollars."
        print(message)
        
        return budget

def main():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
