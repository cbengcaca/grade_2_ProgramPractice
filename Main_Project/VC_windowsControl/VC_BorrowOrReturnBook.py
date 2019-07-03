from M_Hoster.M_Control import MC_BorrowOrReturnBook
from M_Clienter import TcpClienter
class VC_BorrowOrReturnBook:
    def VC_BORB(self,userID,bookID,type):
        list = []
        #a = MC_BorrowOrReturnBook.MC_BorrowOrReturnBook()
        if type == 0:
            list.append("3")
            list.append(str(userID))
            list.append(str(bookID))
            list.append("==")
            a = TcpClienter.TcpClienter()
            list = a.send(list)
            return list[0][0]
        elif type == 1:
            list.append("9")
            list.append(str(bookID))
            list.append("==")
            a = TcpClienter.TcpClienter()
            list = a.send(list)
            return list[0][0]
