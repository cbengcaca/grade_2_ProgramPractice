from TcpClienter import TcpClienter

class VC_downBook:
    def deleteBook(self,infoList):
        sender = TcpClienter()
        ret = sender.send(infoList)
        return ret
