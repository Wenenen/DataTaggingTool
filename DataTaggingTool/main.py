import form
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt

# 没有标注
unlabel = -2

class mywindow(QtWidgets.QMainWindow, form.Ui_mainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.file_path = None
        self.save_file_name = ''
        self.word_list = []
        self.label_list = []
        self.numToLabel = ["错误", "相似", "正确"]
        self.index = 0
        self.is_save = True
        self.yes = 1
        self.soso = 0
        self.no = -1
        self.word_list_len = 0
        QShortcut(QKeySequence(Qt.Key_1), self, self.set_word_yes)
        QShortcut(QKeySequence(Qt.Key_2), self, self.set_word_soso)
        QShortcut(QKeySequence(Qt.Key_3), self, self.set_word_no)
        QShortcut(QKeySequence(Qt.Key_U), self, self.up_word)
        QShortcut(QKeySequence(Qt.Key_S), self, self.save_word)

    # 在label空间上显示词
    # def show_word(self):
    #     self.keyword.setText(self.word_list[self.index])
    #     # self.keyword.show()

    def show_word(self):
        if self.index > 0:
            backStr="前一个的标记为\n" \
                "序号"+str(self.index-1)+"："+self.word_list[self.index-1]+"   标记为了"+str(self.numToLabel[self.label_list[self.index-1]+1])
            self.backLabel.setText(backStr)
        else:
            backStr = "无前一个"
            self.backLabel.setText(backStr)
        self.keyword_cnt.setText(str(self.index))
        self.keyword.setText(self.word_list[self.index])

    # index增加
    def index_up(self):
        if self.index + 1 >= self.word_list_len:
            msg_box = QMessageBox(QMessageBox.Information, "消息提醒", "已经是最后一个了，请保存")
            msg_box.exec_()
            return
        self.index += 1

    # index减少
    def index_down(self):
        if self.index > 0:
            self.index -= 1

    # 文件已经被改变
    def is_change(self):
        self.is_save = False

    # 关键字正确
    def set_word_yes(self):
        if self.file_path is None:
            return
        self.label_list[self.index] = self.yes
        self.index_up()
        self.show_word()
        self.is_change()

    # 关键字相似
    def set_word_soso(self):
        if self.file_path is None:
            return
        self.label_list[self.index] = self.soso
        self.index_up()
        self.show_word()
        self.is_change()

    # 关键字错误
    def set_word_no(self):
        if self.file_path is None:
            return
        self.label_list[self.index] = self.no
        self.index_up()
        self.show_word()
        self.is_change()

    # 回到上一个词
    def up_word(self):
        if self.file_path is None:
            return
        self.index_down()
        self.show_word()

    # 保存文件
    def save_word(self):
        if self.file_path is None:
            return
        tmpstr = ''
        # 保存所有词
        cnt = 0
        for word in self.word_list:
            tmpstr += word
            tmpstr += ' '
            tmpstr += str(self.label_list[cnt])
            tmpstr += '\n'
            cnt += 1

        with open(self.save_file_name, 'w', encoding="utf-8") as f:
            # for word,label in zip(word_list,label_list):
            #     f.write(str(word)+" "+str(label)+"\n")
            f.write(tmpstr)

        self.is_save = True
        msg_box = QMessageBox(QMessageBox.Information, "消息提醒", "保存成功")
        msg_box.exec_()

    def selectTxtFilePath(self):
        # 清空相关变量
        if self.is_save is False:
            reply = QtWidgets.QMessageBox.question(self, '警告', '还未保存，确定重新选文件？',
                                                   QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                pass
            else:
                return
        self.file_name = None
        self.file_path = None
        self.word_list.clear()
        self.label_list.clear()
        self.is_save = True
        self.index = 0
        self.file_path = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd())
        if self.file_path[0]:  # 如果有这个文件
            self.cause_name.setText(os.path.split(self.file_path[0])[1])
            self.save_file_name = self.file_path[0]+"_label"

            with open(self.file_path[0], "r", encoding='utf-8') as txtFile:
                lines = txtFile.readlines()
                for line in lines:
                    line = line.split()
                    self.word_list.append(line[0])
                # 获取label_list
                self.label_list = [unlabel]*len(self.word_list)

            # 判断是否已经标注过
            if os.path.exists(self.save_file_name):
                with open(self.save_file_name, 'r', encoding='utf-8') as save_file:
                    index = 0
                    lines = save_file.readlines()
                    finish = True
                    for line in lines:
                        line = line.split()
                        label = line[1]
                        # 如果没有标注
                        if unlabel == int(label):
                            self.index = index
                            finish = False
                            break
                        self.label_list[index] = int(label)
                        index += 1
                    if finish:
                        self.index = len(self.word_list) - 1

            self.keyword.setText(str(self.word_list[0]))
            self.keyword_cnt.setText("0")
            self.word_list_len = len(self.word_list)
            self.show_word()
            
        else:
            msg_box = QMessageBox(QMessageBox.Information, "消息提醒", "好像没选数据文件噢")
            msg_box.exec_()

    def closeEvent(self, event):
        if self.is_save:
            return
        reply = QtWidgets.QMessageBox.question(self, '警告', '还未保存，确定退出？',
                                           QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
