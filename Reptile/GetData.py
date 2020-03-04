
import json
import requests
import time

from PyQt5.QtCore import QThread, pyqtSignal

from eastUrl import *
class GetData(QThread):
    _signal = pyqtSignal(list)
    def __init__(self,type):
        super(GetData,self).__init__()
        self.type = type
        self.data = list()
        self.Run = True
        self.getKey(type)
    def getKey(self,type):
        if type==1:
            self.key = 'sha'
        elif type==2:
            self.key = 'hk'
        elif type == 3:
            self.key = 'us'
        elif type ==4:
            self.key = 'en'
        elif type == 5:
            self.key = 'asia'
        elif type == 6:
            self.key = 'europe'
        elif type == 7:
            self.key = 'america'
        elif type == 8:
            self.key = 'australia'
        elif type == 9:
            self.key = 'continents'

    def __del__(self):
        self.Run = False
        self.wait()
    def run(self):
        while self.Run:
            self.data.clear()
            # print("====================")
            if self.type==5:
                for i in range(5,10):
                    self.getKey(i)
                    self.Get_Data(2)
                self._signal.emit(self.data)
            else:
                self._signal.emit(self.Get_Data(2))
            self.sleep(2)
    def getPage(self, number):
        '''
                    对目标网站进行数据采集
                    :param number: 采集多少页
                    :return: 采集到的数据
                    '''
        # ff = str()
        # for i in range(200):
        #     ff+="f"+str(i)
        #     print(ff)
        ti = int(time.time() * 1000)
        # strUrl = 'http://2.push2.eastmoney.com/api/qt/clist/get'
        # params = {
        #     'cb': 'jQuery112402418383984387964_1583118307933',
        #     'pn': '1',
        #     'pz': '2500',
        #     'po': '1',
        #     'np': '1',
        #     'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
        #     'fltt': '2',
        #     'invt': '2',
        #     'fid': 'f3',
        #     'fs': 'b:MK0001',
        #     'fields': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f23',
        #     '_': str(ti)
        # }
        eastUrl[self.key]['data']['_'] = str(ti);
        response = requests.get(eastUrl[self.key]['url'], params=eastUrl[self.key]['data'])

        # 处理多余数据方便转换为字典
        data = response.text.replace(eastUrl[self.key]['data']['cb'], '').replace('(', "").replace(')','').replace(';', '')
        # print(self.data)
        return json.loads(data)

    def Get_Data(self, type):
        '''
        对东方财富网抓抓取的数据进行处理
        :return:
        '''
        data = self.getPage(type)
        for t1 in data.get('data').get('diff'):
            # print(t1)
            if self.type>4 and self.type<10:
                list1 = [t1.get('f14'), t1.get('f2'), t1.get('f3'), t1.get('f4'),
                         t1.get('f7'), t1.get('f15'), t1.get('f16'), t1.get('f17'), t1.get('f18'),
                         t1.get('f124'),
                         ]
            else:
                list1 = [t1.get('f12'), t1.get('f14'), t1.get('f2'), t1.get('f3'), t1.get('f4'), t1.get('f5'),
                     t1.get('f6'),
                     t1.get('f7'), t1.get('f15'), t1.get('f16'), t1.get('f17'), t1.get('f18'), t1.get('f10'),
                     t1.get('f8'),
                     t1.get('f9'), t1.get('f23'),
                     # t1.get('f39'),t1.get('f40'),t1.get('f19'),t1.get('f20')
                     ]
            self.data.append(list1)

            # f2最新价 f3涨跌幅 f4涨跌额 f5成交量 f6成交额 f7振幅  f8换手率 f12 代码  f14 名称  f15最高价  f16最低  f17今开 f18昨收  f23 市净率,f10量比 f9市盈率
            # f39卖一 f40买一量 f19买一 20买一量
        # print(self.data)
        return self.data;