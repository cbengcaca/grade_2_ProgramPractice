#from M_Clienter.TcpClienter import TcpClienter
from M_Clienter.TcpClienter import TcpClienter

class VC_SearchBorrowMassage:

    def getBorrowList(self, searchList):
        sender = TcpClienter()
        borrowList = sender.send(searchList)
        return borrowList