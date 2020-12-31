# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 窗口的设置
        # 设置窗口的位置和大小(x, y, 长, 宽)
        self.setGeometry(300, 300, 300, 300)
        # 设置窗口的标题
        self.setWindowTitle('Icontest')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('Icon.JPG'))
        # 显示窗口
        self.show()

        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()  # 默认情况下勾选了checkbox
        cb.stateChanged.connect(self.changeTitle)


        self.show()

    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
