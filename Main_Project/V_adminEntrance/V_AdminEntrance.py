from tkinter import *
from .V_bookAdmin.V_DownBook import V_DownBook
from .V_bookAdmin.V_UpBook import V_UpBook
from .V_workAdmin.V_SearchBorrowMassage import V_SearchBorrowMassage
from .V_workAdmin.V_SearchOverdueMassage import V_SearchOverdueMassage
from .V_workAdmin.V_SearchReader import V_SearchReader
import win32con,win32gui
class V_AdminEntrance():
    def __init__(self,father):
        self.father = father
        self.locate = father.locate
        self.size = father.size
        self.root = Tk()
        self.root.title('ADMIN ENTRANCE')
        self.root.geometry(self.father.size)
        self.root.geometry(self.father.locate)
        self.root.resizable(0,0)


        labelBookAdmin = Label(self.root,text = "Book Admin")
        labelBookAdmin.pack(side = TOP)

        frameButtonAdminBook = Frame(self.root)
        frameButtonAdminBook.pack(side = TOP)

        buttonBookUp = Button(frameButtonAdminBook,text = 'BOOKUP',command = self.openBookUp,font='Consoles')
        buttonBookUp.pack(side = LEFT)
        buttonBookDown = Button(frameButtonAdminBook, text = 'BOOKDOWN',command = self.openBookDown,font='Consoles')
        buttonBookDown.pack(side = LEFT)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)
        labelWorkAdmin = Label(self.root,text = 'Work Admin')
        labelWorkAdmin.pack(side = TOP)

        frameButtonAdminWork = Frame(self.root)
        frameButtonAdminWork.pack(side = TOP)

        buttonSearchReader = Button(frameButtonAdminWork,text = 'SEARCH READER',command = self.openSearchReader,font='Consoles')
        buttonSearchReader.pack(side = LEFT)
        buttonSearchBorrowList = Button(frameButtonAdminWork,text = 'SEARCH BORROW',command = self.openSearchBorrow,font='Consoles')
        buttonSearchBorrowList.pack(side = LEFT)
        buttonSearchOverTime = Button(frameButtonAdminWork,text = 'SEARCH OVERTIME',command = self.openSearchOver,font='Consoles')
        buttonSearchOverTime.pack(side = LEFT)

        labelBlankLast = Label(self.root)
        labelBlankLast.pack(side=BOTTOM)

        buttonReturn = Button(self.root, text='RETURN', command=self.returnFather, font='Consoles')
        buttonReturn.pack(side=BOTTOM)

        mainloop()

    def openBookUp(self):
        self.hideThisWindow()
        bookUp = V_UpBook(self)
        return

    def openBookDown(self):
        self.hideThisWindow()
        bookDown = V_DownBook(self)
        return

    def openSearchReader(self):
        self.hideThisWindow()
        searchReader = V_SearchReader(self)
        return

    def openSearchBorrow(self):
        self.hideThisWindow()
        searchBorrow = V_SearchBorrowMassage(self)
        return

    def openSearchOver(self):
        self.hideThisWindow()
        searchOver = V_SearchOverdueMassage(self)
        return

    def returnFather(self):
        self.father.showThisWindow()
        self.root.destroy()

#win32
    def getWindowHandle(self):
        return win32gui.FindWindow(None,self.root.title())

    def showThisWindow(self):
        win32gui.ShowWindow(self.getWindowHandle(),win32con.SW_SHOW)

    def hideThisWindow(self):
        win32gui.ShowWindow(self.getWindowHandle(),win32con.SW_HIDE)