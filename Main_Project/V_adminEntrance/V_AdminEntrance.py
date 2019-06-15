from tkinter import *
from .V_bookAdmin.V_DownBook import V_DownBook
from .V_bookAdmin.V_UpBook import V_UpBook
from .V_workAdmin.V_SearchBorrowMassage import V_SearchBorrowMassage
from .V_workAdmin.V_SearchOverdueMassage import V_SearchOverdueMassage
from .V_workAdmin.V_SearchReader import V_SearchReader
class V_AdminEntrance():
    def __init__(self):
        self.root = Tk()
        self.root.title('ADMIN ENTRANCE')
        self.root.geometry('400x200')
        self.root.resizable(0,0)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        frameButtonAdminBook = Frame(self.root)
        frameButtonAdminBook.pack(side = TOP)

        buttonBookUp = Button(frameButtonAdminBook,text = 'BOOKUP',command = self.openBookUp)
        buttonBookUp.pack(side = LEFT)
        buttonBookDown = Button(frameButtonAdminBook, text = 'BOOKDOWN',command = self.openBookDown)
        buttonBookDown.pack(side = LEFT)

        labelBlank2 = Label(self.root)
        labelBlank2.pack(side = TOP)

        frameButtonAdminWork = Frame(self.root)
        frameButtonAdminWork.pack(side = TOP)

        buttonSearchReader = Button(frameButtonAdminWork,text = 'SEARCH READER',command = self.openSearchReader)
        buttonSearchReader.pack(side = LEFT)
        buttonSearchBorrowList = Button(frameButtonAdminWork,text = 'SEARCH BORROW',command = self.openSearchBorrow)
        buttonSearchBorrowList.pack(side = LEFT)
        buttonSearchOverTime = Button(frameButtonAdminWork,text = 'SEARCH OVERTIME',command = self.openSearchOver)
        buttonSearchOverTime.pack(side = LEFT)

        mainloop()

    def openBookUp(self):
        bookUp = V_UpBook()
        return

    def openBookDown(self):
        bookDown = V_DownBook()
        return

    def openSearchReader(self):
        searchReader = V_SearchReader()
        return

    def openSearchBorrow(self):
        searchBorrow = V_SearchBorrowMassage()
        return

    def openSearchOver(self):
        searchOver = V_SearchOverdueMassage()
        return