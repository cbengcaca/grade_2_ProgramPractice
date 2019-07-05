from tkinter import *
from V_windows.V_readerEntrance.V_BuyBook import V_BuyBook
from V_windows.V_readerEntrance.V_BorrowOrReturnBook import V_BorrowOrReturnBook


class V_ReaderEntrance():
    def __init__(self):
        self.size = '400x200'
        self.locate = '+20+300'
        self.root = Tk()
        self.root.title('读者入口')
        self.root.geometry(self.size)
        self.root.geometry(self.locate)
        self.root.resizable(0,0)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        buttonBuy = Button(self.root,text = '买书',command = self.openBookBuy,font='Consoles')
        buttonBuy.pack(side = TOP)


        buttonBorrow = Button(self.root,text = '借书/还书',command = self.openBookBorrow,font='Consoles')
        buttonBorrow.pack(side = TOP)

        labelBlank2 = Label(self.root)
        labelBlank2.pack(side=BOTTOM)

        buttonReturn = Button(self.root, text='返回', command=self.returnFather, font='Consoles')
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
