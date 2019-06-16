from tkinter import *
from V_readerEntrance.V_buyBook.V_BuyBook import V_BuyBook
from V_readerEntrance.V_borrowOrReturnBook.V_BorrowOrReturnBook import V_BorrowOrReturnBook
class V_ReaderEntrance():
    def __init__(self,father):
        self.root = Toplevel(father)
        self.root.title('READER ENTRANCE')
        self.root.geometry('400x200')
        self.root.resizable(0,0)
        self.root.attributes("-toolwindow", 1)
        self.root.wm_attributes("-topmost", 1)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        buttonBuy = Button(self.root,text = 'BUYBOOK',command = self.openBookBuy)
        buttonBuy.pack(side = TOP)


        buttonBorrow = Button(self.root,text = 'BORROWBOOK',command = self.openBookBorrow)
        buttonBorrow.pack(side = TOP)

        buttonReturn = Button(self.root,text = 'RETURNBOOK',command = self.openBookReturn)
        buttonReturn.pack(side = TOP)

        mainloop()

    def openBookBuy(self):
        bookBuy = V_BuyBook(self.root)
        return

    def openBookBorrow(self):
        borrowOrReturn = V_BorrowOrReturnBook(0,self.root)
        return

    def openBookReturn(self):
        borrowOrReturn = V_BorrowOrReturnBook(1,self.root)
        return