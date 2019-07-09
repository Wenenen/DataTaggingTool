import form
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox

data_path = 'data/ '


class mywindow(QtWidgets.QMainWindow, form.Ui_mainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.file_path = None
        self.file_name = ''
        self.word_list = []
        self.label_list = [0]*500
        self.numToLabel=["错误","相似","正确"]
        self.index = 0
        self.is_save = False
        self.yes = 1
        self.soso = 0
        self.no = -1

    # 在label空间上显示词
    def show_word(self):
        self.keyword.setText(self.word_list[self.index])
        # self.keyword.show()

    def show_word(self):
        if(self.index>0):
            backStr="前一个的标记为\n" \
                "序号"+str(self.index-1)+"："+self.word_list[self.index-1]+"。  标记为了"+str(self.numToLabel[self.label_list[self.index-1]+1])
            self.backLabel.setText(backStr)
        self.keyword_cnt.setText(str(self.index))
        self.keyword.setText(self.word_list[self.index])


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

    # 上一步操作，供误操作使用
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
            # for word,label in zip(word_list,label_list):
            #     f.write(str(word)+" "+str(label)+"\n")
            f.write(str)
            f.close()

        #清空相关变量
        self.file_name=None
        self.file_path=None
        self.word_list.clear()
        self.label_list = [0] * 500
        self.is_save = True


    def selectTxtFilePath(self):
        self.file_path = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd())
        if self.file_path[0]:
            self.cause_name.setText(os.path.split(self.file_path[0])[1])
            self.file_name = self.file_path[0]+"_label"
            with open(self.file_path[0], "r") as txtFile:
                content = txtFile.readline()
                while(content):
                    content = content.split()
                    self.word_list.append(content[0])
                    content = txtFile.readline()
            self.keyword.setText(self.word_list[0])
            self.keyword_cnt.setText("0")
        else:
            msg_box = QMessageBox(QMessageBox.Information, "消息提醒", "好像没选数据文件噢")
            msg_box.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
