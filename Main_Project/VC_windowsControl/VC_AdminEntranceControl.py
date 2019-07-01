from M_Clienter.TcpClienter import TcpClienter
class VC_AdminEntranceControl:

    def getLogKeyToCompare(self,logkey):
        sender = TcpClienter()
        recList = sender.send(logkey)
        return recList[0]



