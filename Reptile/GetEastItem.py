import requests


class GetEastItem:
    def __init__(self):
        pass

    def setTask(self):
        pass

    # def doTask(self):
    #     #分时线接口
    #     strUrl = 'http://push2.eastmoney.com/api/qt/stock/trends2/get'
    #     params = {
    #         'cb': 'jQuery1124042513914550779375_1578882361468',
    #         'fields1': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13',
    #         'fields2':'f51,f52,f53,f54,f55,f56,f57,f58',
    #         'ut':'fa5fd1943c7b386f172d6893dbfba10b' ,
    #         'ndays': '1' ,
    #         'iscr':'0' ,
    #         'secid':'1.603286',
    #         '_': '1578882361472'
    #     }
    #     response = requests.get(strUrl,params=params)
    #     data = response.text.replace("jQuery1124042513914550779375_1578882361468", '').replace('(', "").replace(')','').replace(';', '')
    #
    #     print(data)


    def doTask(self):
        #分时线接口
        strUrl = 'http://push2.eastmoney.com/api/qt/stock/get'
        params = {
            'ut':'fa5fd1943c7b386f172d6893dbfba10b',
            'invt':'2',
            'fltt':'2',
            'fields':'f43,f57,f58,ctp,f170,f46,f44,f51,f168,f47,f164,f163,f116,f60,f45,f52,f50,f48,f167,f117,f71,f161,f49,f530,f135,f136,f137,f138,f139,f141,f142,f144,f145,f147,f148,f140,f143,f146,f149,f55,f62,f162,f92,f173,f104,f105,f84,f85,f183,f184,f185,f186,f187,f188,f189,f190,f191,f192,f107,f111,f86,f177,f78,f110,f262,f263,f264,f267,f268,f250,f251,f252,f253,f254,f255,f256,f257,f258,f266,f269,f270,f271,f273,f274,f275,f127,f199,f128,f193,f196,f194,f195,f197,f80,f280,f281,f282,f284,f285,f286,f287',
            'secid':'0.002599',
            'cb':'jQuery112405831440079032297_1578892365285',
            '_':'1578892365407'
        }
        response = requests.get(strUrl,params=params)
        data = response.text.replace("jQuery112405831440079032297_1578892365285", '').replace('(', "").replace(')','').replace(';', '')
        #f43：最新价
        # f44：最高
        #f45:最低
        #f46:今开
        # f47:成交量
        #f48：成交额
        # f50:量比
        # f51：涨停
        # f52：跌停
        #f60：昨收
        # f116：总市值
        # f117：流通市值
        # f162：市盈动
        # f167：市净
        #f168：换手

        print(data)

#http://push2.eastmoney.com/api/qt/stock/get?ut=fa5fd1943c7b386f172d6893dbfba10b&invt=2&fltt=2&fields=f43,f57,f58,f169,f170,f46,f44,f51,f168,f47,f164,f163,f116,f60,f45,f52,f50,f48,f167,f117,f71,f161,f49,f530,f135,f136,f137,f138,f139,f141,f142,f144,f145,f147,f148,f140,f143,f146,f149,f55,f62,f162,f92,f173,f104,f105,f84,f85,f183,f184,f185,f186,f187,f188,f189,f190,f191,f192,f107,f111,f86,f177,f78,f110,f262,f263,f264,f267,f268,f250,f251,f252,f253,f254,f255,f256,f257,f258,f266,f269,f270,f271,f273,f274,f275,f127,f199,f128,f193,f196,f194,f195,f197,f80,f280,f281,f282,f284,f285,f286,f287&secid=0.002641&cb=jQuery112405831440079032297_1578892365285&_=1578892365407
if __name__ == '__main__':
    item = GetEastItem()
    item.doTask();