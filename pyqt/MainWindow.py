from PyQt5.QtWidgets import QWidget, QTabWidget, QHBoxLayout

from pyqt.Borad import Board
from pyqt.IndexMarket import IndexMarket


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.tab = QTabWidget(self)
        self.sha = Board(1)
        self.hk = Board(2)
        self.us = Board(3)
        self.en = Board(4)
        self.index = IndexMarket()
        self.InitLayout()


    def InitLayout(self):
        self.h_layout = QHBoxLayout(self)
        self.h_layout.setSpacing(20)
        self.h_layout.setStretch(20, 20)
        self.h_layout.addWidget(self.tab, 1)
        self.tab.addTab(self.sha,"沪深A股")
        self.tab.addTab(self.hk, "港股主板")
        self.tab.addTab(self.us, "美股")
        self.tab.addTab(self.en, "英股")
        self.tab.addTab(self.index, "指数")