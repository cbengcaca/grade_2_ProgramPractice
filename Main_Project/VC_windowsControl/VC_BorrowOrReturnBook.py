import V_BorrowOrReturnBook
import MC_BorrowOrReturnBook

class VC_BorrowOrReturnBook:
    def VC_BORB(self,userID,bookID,type):
        a = MC_BorrowOrReturnBook.MC_BorrowOrReturnBook()
        if type == 0:
            return a.Borrow(userID,bookID)
        elif type == 1:
            return a.Return(bookID)
