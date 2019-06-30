from sendToServ import SendToServ

class C_BuyBook:
    def __init__(self, bookId):
        self.__bookId = bookId
        self.__sendToServ = SendToServ()     #生成一个对象

    #向服务器发送购买书籍请求
    def sendMessage(self):
        dataList = ['2', self.__bookId, '==']
        ret = self.__sendToServ.send(dataList, '192.168.56.1')
        return ret