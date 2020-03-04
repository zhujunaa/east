import time
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QTableWidget, QHBoxLayout, QHeaderView, QAbstractItemView, QTableWidgetItem

from Reptile.GetData import GetData


class IndexMarket(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.data = GetData(5)
        self.data._signal.connect(self.updateData)  # 连接信号
        self.data.start()
        self.first = 1

        self.idsTable = QTableWidget(self)
        self.InitTables()
        self.h_layout = QHBoxLayout(self)
        self.h_layout.setSpacing(20)
        self.h_layout.setStretch(20, 20)
        self.h_layout.addWidget(self.idsTable)
        # self.getData()

        # self.timer = QTimer(self)  # 初始化一个定时器
        # self.timer.timeout.connect(self.updateData)  # 计时结束调用operate()方法
        # self.timer.start(2000)  # 设置计时间隔并启动

    def InitTables(self):
        ids = ['名称', '最新价', '涨跌幅', '涨跌额', '振幅', '最高', '最低', '今开', '昨收', '时间'
               # '卖一价','卖一量','买一价','买一量'
               ]
        self.idsTable.setColumnCount(len(ids))
        self.idsTable.setHorizontalHeaderLabels(ids)
        self.idsTable.setEditTriggers(QAbstractItemView.NoEditTriggers);  # 不可编辑
        self.idsTable.setSelectionMode(QAbstractItemView.SingleSelection);  # 设置选择模式，选择单行
        self.idsTable.setSelectionBehavior(QAbstractItemView.SelectRows);  # 设置选择行为，以行为单位
        self.idsTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents);
        self.idsTable.horizontalHeader().setStretchLastSection(True);
        self.idsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch);
        self.idsTable.horizontalHeader().setSectionsClickable(False);  # 设置表头不可点击
        self.idsTable.setRowCount(300)
    # def GetAllData(self):
    #     self.eastData.clear();
    #     for item in self.datas:
    #         self.eastData+=item.Get_Data(2)
    def getData(self,eastData):
        row = 0
        for data in eastData:
            self.idsTable.setItem(row, 0, QTableWidgetItem(data[0]))
            self.idsTable.setItem(row, 1, QTableWidgetItem(str(data[1])))
            self.idsTable.setItem(row, 2, QTableWidgetItem(str(data[2])))
            self.idsTable.setItem(row, 3, QTableWidgetItem(str(data[3])))
            self.idsTable.setItem(row, 4, QTableWidgetItem(str(data[4])))
            self.idsTable.setItem(row, 5, QTableWidgetItem(str(data[5])))
            self.idsTable.setItem(row, 6, QTableWidgetItem(str(data[6])))
            self.idsTable.setItem(row, 7, QTableWidgetItem(str(data[7])))
            self.idsTable.setItem(row, 8, QTableWidgetItem(str(data[8])))
            timeArray = time.localtime(data[9])
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            self.idsTable.setItem(row, 9, QTableWidgetItem(otherStyleTime))
            row += 1
            # print(data)

    def updateData(self,eastData):
        if self.first ==1 :
            self.getData(eastData)
            self.first = 0
            return
        row = 0
        for data in eastData:
            self.idsTable.item(row, 0).setText(data[0])
            self.idsTable.item(row, 1).setText(str(data[1]))
            self.idsTable.item(row, 2).setText(str(data[2]))
            self.idsTable.item(row, 3).setText(str(data[3]))
            self.idsTable.item(row, 4).setText(str(data[4]))
            self.idsTable.item(row, 5).setText(str(data[5]))
            self.idsTable.item(row, 6).setText(str(data[6]))
            self.idsTable.item(row, 7).setText(str(data[7]))
            self.idsTable.item(row, 8).setText(str(data[8]))
            timeArray = time.localtime(data[9])
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            self.idsTable.item(row, 9).setText(otherStyleTime)

            row += 1