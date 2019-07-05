from M_Clienter.TcpClienter import TcpClienter
class VC_UpBook:
    def searchIsbnExist(self,infoList):
        sender = TcpClienter()
        ret = sender.send(infoList)
        ##isbn存在
        if ret[0][0] is '1' :
            return '1'
        ##isbn不存在
        else :
        ##二维列表返回
            return ret

    def addBookExist(self,infoList):
        sender = TcpClienter()
        bookId = sender.send(infoList)
        #判断成功依据
        return bookId[0][0]

    def addBookNotExist(self,infoList):
        sender = TcpClienter()
        bookId = sender.send(infoList)
        ##返回值不为0则添加成功
        return bookId[0][0]