from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QTableWidget, QHBoxLayout, QTableWidgetItem, QAbstractItemView, QHeaderView

from Reptile.GetData import GetData


class Board(QWidget):
    def __init__(self,type):
        QWidget.__init__(self)
        self.idsTable = QTableWidget(self)
        self.h_layout = QHBoxLayout(self)
        self.h_layout.setSpacing(20)
        self.h_layout.setStretch(20, 20)
        self.h_layout.addWidget(self.idsTable, 1)
        self.data = GetData(type)
        self.data._signal.connect(self.updateData)  # 连接信号
        self.first = 1
        self.data.start()
        self.InitTableIds(type);

        # self.getData()

        # self.timer = QTimer(self)  # 初始化一个定时器
        # self.timer.timeout.connect(self.updateData)  # 计时结束调用operate()方法
        #
        # self.timer.start(2000)  # 设置计时间隔并启动


    def InitTableIds(self,type):
        ids = ['id', '名称', '最新价', '涨跌幅', '涨跌额', '成交量', '成交额', '振幅', '最高', '最低', '今开', '昨收', '量比', '换手率', '市盈率', '市净率',
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
        if type==1:
            self.idsTable.setRowCount(4000)
        elif type == 2:
            self.idsTable.setRowCount(2500)
        elif type==3:
            self.idsTable.setRowCount(500)
        elif type ==4:
            self.idsTable.setRowCount(300)

    def getData(self ,eastData):
        row = 0
        for data in eastData:
            self.idsTable.setItem(row, 0, QTableWidgetItem(data[0]))
            self.idsTable.setItem(row, 1, QTableWidgetItem(data[1]))
            self.idsTable.setItem(row, 2, QTableWidgetItem(str(data[2])))
            self.idsTable.setItem(row, 3, QTableWidgetItem(str(data[3])))
            self.idsTable.setItem(row, 4, QTableWidgetItem(str(data[4])))
            self.idsTable.setItem(row, 5, QTableWidgetItem(str(data[5])))
            self.idsTable.setItem(row, 6, QTableWidgetItem(str(data[6])))
            self.idsTable.setItem(row, 7, QTableWidgetItem(str(data[7])))
            self.idsTable.setItem(row, 8, QTableWidgetItem(str(data[8])))
            self.idsTable.setItem(row, 9, QTableWidgetItem(str(data[9])))
            self.idsTable.setItem(row, 10, QTableWidgetItem(str(data[10])))
            self.idsTable.setItem(row, 11, QTableWidgetItem(str(data[11])))
            self.idsTable.setItem(row, 12, QTableWidgetItem(str(data[12])))
            self.idsTable.setItem(row, 13, QTableWidgetItem(str(data[13])))
            self.idsTable.setItem(row, 14, QTableWidgetItem(str(data[14])))
            self.idsTable.setItem(row, 15, QTableWidgetItem(str(data[15])))
            # self.idsTable.setItem(row, 16, QTableWidgetItem(str(data[16])))
            # self.idsTable.setItem(row, 17, QTableWidgetItem(str(data[17])))
            # self.idsTable.setItem(row, 18, QTableWidgetItem(str(data[18])))
            # self.idsTable.setItem(row, 19, QTableWidgetItem(str(data[19])))
            row += 1
            # print(data)

    def updateData(self,eastData):
        # print(self.eastData)
        if self.first==1:
            self.getData(eastData)
            self.first = 0
            return
        row = 0
        for data in eastData:
            self.idsTable.item(row, 0).setText(data[0])
            self.idsTable.item(row, 1).setText(data[1])
            self.idsTable.item(row, 2).setText(str(data[2]))
            self.idsTable.item(row, 3).setText(str(data[3]))
            self.idsTable.item(row, 4).setText(str(data[4]))
            self.idsTable.item(row, 5).setText(str(data[5]))
            self.idsTable.item(row, 6).setText(str(data[6]))
            self.idsTable.item(row, 7).setText(str(data[7]))
            self.idsTable.item(row, 8).setText(str(data[8]))
            self.idsTable.item(row, 9).setText(str(data[9]))
            self.idsTable.item(row, 10).setText(str(data[10]))
            self.idsTable.item(row, 11).setText(str(data[11]))
            self.idsTable.item(row, 12).setText(str(data[12]))
            self.idsTable.item(row, 13).setText(str(data[13]))
            self.idsTable.item(row, 14).setText(str(data[14]))
            self.idsTable.item(row, 15).setText(str(data[15]))
            # self.idsTable.item(row, 16).setText(str(data[16]))
            # self.idsTable.item(row, 17).setText(str(data[17]))
            # self.idsTable.item(row, 18).setText(str(data[18]))
            # self.idsTable.item(row, 19).setText(str(data[19]))
            row += 1