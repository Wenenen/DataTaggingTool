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
        self.file_name = ''
        self.word_list = []
        self.label_list = []
        self.index = 0

    def show_word(self,index):
        pass

    # index增加
    def index_up(self):
        self.index += 1

    # index减少
    def index_down(self):
        self.index -= 1

    # 关键字正确，正确设置为 1
    def set_word_yes(self):
        self.label_list[self.index] = 1
        self.index_up()

    # 关键字相似,相似设置为 0
    def set_word_soso(self):
        self.label_list[self.index] = 0
        self.index_up()

    # 关键字错误，错误设置为 -1
    def set_word_no(self):
        self.label_list[self.index] = -1
        self.index_up()

    def up_word(self):
        self.index_down()

    def save_word(self):
        str = ''
        for i in range(self.index):
            str += self.word_list[i]
            str += ' '
            str += self.label_list[i]
            str += '\n'
        with open(self.file_name, 'w') as f:
            f.write(str)
            f.close()



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