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
    def __init__(self):
        self.root = Tk()
        self.id = ''
        self.pwd = ''


        self.locate = '+400+200'
        self.size = '500x300'

        self.root.title('ADMIN ENTRANCE')
        self.root.geometry(self.size)
        self.root.geometry(self.locate)
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

        buttonFrame = Frame(self.root)
        buttonFrame.pack(side = BOTTOM)
        buttonLogin = Button(buttonFrame,text = "LOGIN", command = self.adminLogin, font = 'Consoles')
        buttonLogin.pack(side = LEFT)
        buttonReturn = Button(buttonFrame, text='return', command=self.selfDestory, font='Consoles')
        buttonReturn.pack(side= LEFT)

        mainloop()

    def openBookUp(self):
        bookUp = V_UpBook(self.id)
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

    def adminLogin(self):
        if self.id is not '':
            messagebox.showerror(message= 'Is already login')
            return
        else:
            logWindow = C_GetLogin()
            self.logKey = []
            self.logKey = logWindow.getLogin()

            if self.logKey[0] == '' or self.logKey[1] == '':
                self.selfDestory()
                return

            self.logKey.insert(0, '11')
            controler = VC_AdminEntranceControl()
            result = controler.getLogKeyToCompare(self.logKey)
            if result[0] is '0':
                self.selfDestory()
                return
            else:
                self.id = self.logKey[1]
                self.pwd = self.logKey[2]
                self.root.title(self.logKey[1])

    def selfDestory(self):
        self.root.quit()
        self.root.destroy()




