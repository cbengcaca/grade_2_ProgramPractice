from tkinter import *

class V_Login:

    def __init__(self , fGet ):
        self.__fGet = fGet
        self.root = Toplevel()
        self.root.title('登录')
        self.root.resizable(0,0)
        self.root.geometry('400x200')
        self.root.attributes("-toolwindow", 1)
        self.root.wm_attributes("-topmost", 1)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        frameUserNumber = Frame(self.root)
        frameUserNumber.pack(side = TOP)
        labelUserNumber = Label(frameUserNumber,text = '管理员ID:',font = 'Consoles')
        self.__userNumber = StringVar()
        entryUserNumber = Entry(frameUserNumber,textvariable = self.__userNumber)
        labelUserNumber.pack(side = LEFT)
        entryUserNumber.pack(side = RIGHT)

        labelBlank2 = Label(self.root)
        labelBlank2.pack(side = TOP)

        frameUserPwd = Frame(self.root)
        frameUserPwd.pack(side = TOP)
        labelUserPwd = Label(frameUserPwd,text = '管理员密码:', font = 'Consoles')
        self.__userPwd = StringVar()
        entryUserPwd = Entry(frameUserPwd,textvariable = self.__userPwd)
        labelUserPwd.pack(side = LEFT)
        entryUserPwd.pack(side = RIGHT)
        entryUserPwd['show'] = '*'

        labelBlank3 = Label(self.root)
        labelBlank3.pack(side = TOP)

        frameButton = Frame(self.root)
        frameButton.pack(side = TOP)
        buttonConfirm = Button(frameButton,text = '确认',command = self.sendOutInput, font = 'Consoles')
        buttonConfirm.pack(side = LEFT)

        mainloop()

    def getInput(self):
        loginId = self.__userNumber.get()
        loginPwd = self.__userPwd.get()
        login = [loginId,loginPwd]
        return login

    def sendOutInput(self):
        self.__fGet.setLogin(self.getInput())
        self.root.quit()
        self.root.destroy()
        return


class C_GetLogin():
    def __init__(self):
        self.__logKey = ['','']


    def setLogin(self,logKey):
        self.__logKey = logKey

    def getLogin(self):
        v = V_Login(self)
        return self.__logKey

