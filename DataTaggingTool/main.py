import form
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox

data_path = 'data/ '

class mywindow(QtWidgets.QMainWindow,form.Ui_mainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.file_path = ''
        self.word_list = []
        self.label_list = []
        self.index = 0

    def set_word_no(self):
        print(1)

    def selectTxtFilePath(self):
        filePath = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd())
        if filePath[0]:
            if (filePath[0].split('.')[1] == 'txt'):
                pass
            else:
                msg_box = QMessageBox(QMessageBox.Information, "消息提醒", "数据文件好像选错了")
                msg_box.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())