from tkinter import *
from V_readerEntrance.V_buyBook.V_BuyBook import V_BuyBook
from V_readerEntrance.V_borrowOrReturnBook.V_BorrowOrReturnBook import V_BorrowOrReturnBook
import win32gui,win32con

class V_ReaderEntrance():
    def __init__(self,father):
        self.size = father.size
        self.locate = father.locate
        self.father = father
        self.root = Tk()
        self.root.title('READER ENTRANCE')
        self.root.geometry(self.size)
        self.root.geometry(self.locate)
        self.root.resizable(0,0)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        buttonBuy = Button(self.root,text = 'BUY BOOK',command = self.openBookBuy,font='Consoles')
        buttonBuy.pack(side = TOP)


        buttonBorrow = Button(self.root,text = 'BORROW BOOK',command = self.openBookBorrow,font='Consoles')
        buttonBorrow.pack(side = TOP)

        buttonReturn = Button(self.root,text = 'RETURN BOOK',command = self.openBookReturn,font='Consoles')
        buttonReturn.pack(side = TOP)

        labelBlank2 = Label(self.root)
        labelBlank2.pack(side=BOTTOM)

        buttonReturn = Button(self.root, text='RETURN', command=self.returnFather, font='Consoles')
        buttonReturn.pack(side=BOTTOM)

        mainloop()

    def openBookBuy(self):
        self.hideThisWindow()
        bookBuy = V_BuyBook(self)
        return

    def openBookBorrow(self):
        self.hideThisWindow()
        borrowOrReturn = V_BorrowOrReturnBook(0,self)
        return

    def openBookReturn(self):
        self.hideThisWindow()
        borrowOrReturn = V_BorrowOrReturnBook(1,self)
        return

    def returnFather(self):
        self.father.showThisWindow()
        self.root.destroy()


    def getWindowHandle(self):
        return win32gui.FindWindow(None, self.root.title())

    def showThisWindow(self):
        win32gui.ShowWindow(self.getWindowHandle(), win32con.SW_SHOW)

    def hideThisWindow(self):
        win32gui.ShowWindow(self.getWindowHandle(), win32con.SW_HIDE)