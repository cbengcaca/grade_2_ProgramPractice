from tkinter import *
from tkinter import messagebox
from V_windows.V_adminEntrance.V_DownBook import V_DownBook
from V_windows.V_adminEntrance.V_UpBook import V_UpBook
from V_windows.V_adminEntrance.V_SearchBorrowMassage import V_SearchBorrowMassage
from V_windows.V_adminEntrance.V_SearchOverdueMassage import V_SearchOverdueMassage
from V_windows.V_adminEntrance.V_SearchReader import V_SearchReader
from VC_windowsControl.VC_AdminEntranceControl import VC_AdminEntranceControl
from V_windows.V_adminEntrance.C_GetLogin import C_GetLogin
import win32con,win32gui
class V_AdminEntrance():
    def __init__(self,father):
        self.father = father
        self.root = Tk()
        logWindow = C_GetLogin()
        self.logKey = []
        self.logKey = logWindow.getLogin()
        self.logKey.insert(0,'9')
        controler = VC_AdminEntranceControl()
        result = controler.getLogKeyToCompare(self.logKey)
        if result[0] is '0':
            self.returnFather()

        self.locate = father.locate
        self.size = father.size

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

        buttonReturn = Button(self.root, text='RETURN', command=self.destoryAndReturn, font='Consoles')
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

    def selfDestory(self):
        self.root.quit()
        self.root.destroy()

    def destoryAndReturn(self):
        self.returnFather()
        self.selfDestory()

#win32
    def getWindowHandle(self):
        return win32gui.FindWindow(None,self.root.title())

    def showThisWindow(self):
        win32gui.ShowWindow(self.getWindowHandle(),win32con.SW_SHOW)

    def hideThisWindow(self):
        win32gui.ShowWindow(self.getWindowHandle(),win32con.SW_HIDE)

