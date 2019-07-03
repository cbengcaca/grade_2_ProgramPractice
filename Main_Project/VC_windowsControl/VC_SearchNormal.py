from M_Clienter.TcpClienter import TcpClienter

class VC_SearchNormal:

    def __init__(self):
        self.bookList = []

    def sendSearchToTcp(self, v_searchPlus, searchList):
        tcpClienter = TcpClienter()
        self.bookList = tcpClienter.send(searchList)
        self.viewBookInformation(v_searchPlus)

    def viewBookInformation(self,v_searchPlus):
        v_searchPlus.setBookInformation(self.bookList)