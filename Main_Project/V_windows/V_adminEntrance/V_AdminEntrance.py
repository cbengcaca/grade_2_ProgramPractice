from tkinter import *
from tkinter import messagebox
from V_windows.V_adminEntrance.V_DownBook import V_DownBook
from V_windows.V_adminEntrance.V_UpBook import V_UpBook
from V_windows.V_adminEntrance.V_SearchBorrowMassage import V_SearchBorrowMassage
from V_windows.V_adminEntrance.V_SearchReader import V_SearchReader
from VC_windowsControl.VC_AdminEntranceControl import VC_AdminEntranceControl
from V_windows.V_adminEntrance.C_GetLogin import C_GetLogin

class V_AdminEntrance():
    def __init__(self):
        self.root = Tk()
        self.id = ''
        self.pwd = ''


        self.locate = '+400+200'
        self.size = '500x300'

        self.root.title('管理员入口')
        self.root.geometry(self.size)
        self.root.geometry(self.locate)
        self.root.resizable(0,0)


        labelBookAdmin = Label(self.root)
        labelBookAdmin.pack(side = TOP)

        frameButtonAdminBook = Frame(self.root)
        frameButtonAdminBook.pack(side = TOP)

        self.buttonBookUp = Button(frameButtonAdminBook,text = '书籍上架',command = self.openBookUp,font='Consoles')
        self.buttonBookUp.pack(side = LEFT)
        self.buttonBookDown = Button(frameButtonAdminBook, text = '书籍下架',command = self.openBookDown,font='Consoles')
        self.buttonBookDown.pack(side = LEFT)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)
        # labelWorkAdmin = Label(self.root,text = 'Work Admin')
        # labelWorkAdmin.pack(side = TOP)

        frameButtonAdminWork = Frame(self.root)
        frameButtonAdminWork.pack(side = TOP)

        self.buttonSearchReader = Button(frameButtonAdminWork,text = '读者信息浏览',command = self.openSearchReader,font='Consoles')
        self.buttonSearchReader.pack(side = LEFT)
        self.buttonSearchBorrowList = Button(frameButtonAdminWork,text = '借阅信息浏览',command = self.openSearchBorrow,font='Consoles')
        self.buttonSearchBorrowList.pack(side = LEFT)
        # buttonSearchOverTime = Button(frameButtonAdminWork,text = 'SEARCH OVERTIME',command = self.openSearchOver,font='Consoles')
        # buttonSearchOverTime.pack(side = LEFT)

        labelBlankLast = Label(self.root)
        labelBlankLast.pack(side=BOTTOM)

        buttonFrame = Frame(self.root)
        buttonFrame.pack(side = BOTTOM)
        self.buttonLogin = Button(buttonFrame,text = "管理员登录", command = self.adminLogin, font = 'Consoles')
        self.buttonLogin.pack(side = LEFT)
        self.buttonReturn = Button(buttonFrame, text='返回', command=self.selfDestory, font='Consoles')
        self.buttonReturn.pack(side= LEFT)

        self.setButtonState(False)

        mainloop()

    def setButtonState(self,bool):
        if bool == False:
            self.buttonBookUp['state'] = DISABLED
            self.buttonBookDown['state'] = DISABLED
            self.buttonSearchReader['state'] = DISABLED
            self.buttonSearchBorrowList['state'] = DISABLED
        else:
            self.buttonBookUp['state'] = NORMAL
            self.buttonBookDown['state'] = NORMAL
            self.buttonSearchReader['state'] = NORMAL
            self.buttonSearchBorrowList['state'] = NORMAL

    def openBookUp(self):
        bookUp = V_UpBook(self.id)
        return

    def openBookDown(self):
        bookDown = V_DownBook(self.id)
        return

    def openSearchReader(self):
        searchReader = V_SearchReader()
        return

    def openSearchBorrow(self):
        searchBorrow = V_SearchBorrowMassage()
        return


    def adminLogin(self):
        if self.id is not '':
            messagebox.showerror(message= '无法重复登录')
            return
        else:
            logWindow = C_GetLogin()
            self.logKey = []
            self.logKey = logWindow.getLogin()

            if self.logKey[0] == '' or self.logKey[1] == '':
                messagebox.showerror(message='登录有误')
                self.selfDestory()
                return

            self.logKey.insert(0, '11')
            controler = VC_AdminEntranceControl()
            result = controler.getLogKeyToCompare(self.logKey)
            if result[0] is '0':

                self.selfDestory()
                return
            else:
                messagebox.showinfo(message= '登录成功')
                self.id = self.logKey[1]
                self.pwd = self.logKey[2]
                self.root.title(self.logKey[1])
                self.setButtonState(True)

    def selfDestory(self):
        self.root.quit()
        self.root.destroy()




