import form
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

data_path = 'data/ '


class mywindow(QtWidgets.QMainWindow, form.Ui_mainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.file_path = ''
        self.file_name = ''
        self.word_list = []
        self.label_list = []
        self.index = 0
        self.is_save = False
        self.yes = 1
        self.soso = 0
        self.no = -1

    # 在label空间上显示词
    def show_word(self):
        self.keyword.setText(self.word_list[self.index])
        # self.keyword.show()

    # 显示计数器
    def show_word_cnt(self):
        self.keyword_cnt.setText(self.index)
        # self.keyword_cnt.show()

    # index增加
    def index_up(self):
        self.index += 1

    # index减少
    def index_down(self):
        if self.index > 0:
            self.index -= 1

    # 关键字正确
    def set_word_yes(self):
        self.label_list[self.index] = self.yes
        self.index_up()
        self.show_word()

    # 关键字相似
    def set_word_soso(self):
        self.label_list[self.index] = self.soso
        self.index_up()
        self.show_word()

    # 关键字错误，错误设置为 -1
    def set_word_no(self):
        self.label_list[self.index] = self.no
        self.index_up()
        self.show_word()

    # 回到上一个词
    def up_word(self):
        self.index_down()
        self.show_word()

    # 展示确定
    def showDialog(self, message):
        msg_box = QMessageBox(QMessageBox.Informationm, '保存成功')
        msg_box.show()
        msg_box.exec_()

    # 保存文件
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
        self.is_save = True


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
