import form
import sys
from PyQt5 import QtWidgets

data_path = 'data/ '

class mywindow(QtWidgets.QMainWindow,form.Ui_mainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())