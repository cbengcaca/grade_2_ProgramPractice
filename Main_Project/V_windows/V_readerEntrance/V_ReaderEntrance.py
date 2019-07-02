from tkinter import *
from V_windows.V_readerEntrance.V_BuyBook import V_BuyBook
from V_windows.V_readerEntrance.V_BorrowOrReturnBook import V_BorrowOrReturnBook
import win32gui,win32con

class V_ReaderEntrance():
    def __init__(self):
        self.size = '400x200'
        self.locate = '+400+200'
        self.root = Tk()
        self.root.title('READER ENTRANCE')
        self.root.geometry(self.size)
        self.root.geometry(self.locate)
        self.root.resizable(0,0)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        buttonBuy = Button(self.root,text = 'BUY BOOK',command = self.openBookBuy,font='Consoles')
        buttonBuy.pack(side = TOP)


        buttonBorrow = Button(self.root,text = 'BORROW/RETURN',command = self.openBookBorrow,font='Consoles')
        buttonBorrow.pack(side = TOP)

        labelBlank2 = Label(self.root)
        labelBlank2.pack(side=BOTTOM)

        buttonReturn = Button(self.root, text='RETURN', command=self.returnFather, font='Consoles')
        buttonReturn.pack(side=BOTTOM)

        mainloop()

    def openBookBuy(self):
        bookBuy = V_BuyBook()
        return

    def openBookBorrow(self):
        borrowOrReturn = V_BorrowOrReturnBook()
        return

    def returnFather(self):
        self.root.quit()
        self.root.destroy()
