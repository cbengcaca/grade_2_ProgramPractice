from sendToServ import SendToServ

class C_BuyBook:
    def __init__(self):
        self.__sendToServ = SendToServ()     #生成一个对象

    #向服务器发送购买书籍请求
    def sendBuyMessage(self, bookId, payFlag):
        dataList = ['2']
        dataList.append(str(bookId))
        dataList.append(str(payFlag))
        dataList.append('==')
        ret = self.__sendToServ.send(dataList, '192.168.56.1')[0][0]
        return ret

if __name__ == '__main__':
    c = C_BuyBook()
    ret = c.sendBuyMessage(12, 1)
    print(ret)