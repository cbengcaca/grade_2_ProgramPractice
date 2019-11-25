from M_Clienter.TcpClienter import TcpClienter

class VC_BuyBook:
    def __init__(self):
        self.__sendToServ =TcpClienter()     #生成一个对象

    #向服务器发送购买书籍请求
    def sendBuyMessage(self, bookId, payFlag):
        dataList = ['2']
        dataList.append(str(bookId))
        dataList.append(str(payFlag))
        dataList.append('==')
        ret = self.__sendToServ.send(dataList)[0][0]
        return ret

if __name__ == '__main__':
    c = VC_BuyBook()
    ret = c.sendBuyMessage('12', 1)
    print(ret)