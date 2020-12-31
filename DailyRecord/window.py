# -*- coding: utf-8 -*-

'''
Author: mxh970120
Date: 2020.12.31
'''

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QGridLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import numpy as np


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # QGridLayout的实例被创建并设置应用程序窗口的布局。
        grid = QGridLayout()
        self.setLayout(grid)
        # 设定属性
        attributes = np.array([["学习", "没学习", "<1h", "1h~2h", ">2h"],
                              ["走路", "没走路", "<1万步", "1万步~10公里", ">10公里"],
                              ["编程", "没编程", "<1h", "1h~2h", ">2h"],
                              ["德语", "看了", "没看"],
                              ["英语", "看了", "没看"]])

        for i in range(len(attributes)):
            for j, value in enumerate(attributes[i]):
                if j == 0:
                    print(j, value)
                    button = QPushButton(value)
                    grid.addWidget(button, i, j)
                else:
                    cb = QCheckBox(value, self)
                    cb.stateChanged.connect(self.changeTitle)
                    grid.addWidget(cb, i, j)

        verifyBtn = QPushButton("确定")
        verifyBtn.clicked.connect(self.changeTitle)
        grid.addWidget(verifyBtn, len(attributes), 5)

        # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        # 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
        # for position, name in zip(positions, names):
        #
        #     if name == '':
        #         continue
        #     button = QPushButton(name)
        #     # 创建按钮并使用addWidget()方法添加到布局中。
        #     grid.addWidget(button, *position)





        # 窗口的设置
        # 设置窗口的位置和大小(x, y, 长, 宽)
        self.setGeometry(300, 300, 300, 300)
        # 设置窗口的标题
        self.setWindowTitle('Icontest')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('Icon.JPG'))
        # 显示窗口
        self.show()

    def changeTitle(self, state):
        sender = self.sender()
        if state == Qt.Checked:
            self.setWindowTitle(sender.text())
        else:
            self.setWindowTitle('')

    def verity(self, state):
        sender = self.sender()
        if state == Qt.Checked:
            self.setWindowTitle(sender.text())
        else:
            self.setWindowTitle('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
