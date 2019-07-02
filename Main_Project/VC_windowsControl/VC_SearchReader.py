from M_Clienter.TcpClienter import TcpClienter
class VC_SearchReader:
    def beginSearchReader(self):
        sender = TcpClienter()
        infoList = ['6']
        ret = sender.send(infoList)
        return ret