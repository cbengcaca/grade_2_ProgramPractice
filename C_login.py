from tkinter import *

class V_login:

    def __init__(self , fGet):
        self.__fGet = fGet
        self.__root = Tk()
        self.__root.title('LOGIN')
        self.__root.resizable(0,0)
        self.__root.geometry('400x200')

        labelBlank1 = Label(self.__root)
        labelBlank1.pack(side = TOP)

        frameUserNumber = Frame(self.__root)
        frameUserNumber.pack(side = TOP)
        labelUserNumber = Label(frameUserNumber,text = 'NUMBER:')
        self.__userNumber = StringVar()
        entryUserNumber = Entry(frameUserNumber,textvariable = self.__userNumber)
        labelUserNumber.pack(side = LEFT)
        entryUserNumber.pack(side = RIGHT)

        labelBlank2 = Label(self.__root)
        labelBlank2.pack(side = TOP)

        frameUserPwd = Frame(self.__root)
        frameUserPwd.pack(side = TOP)
        labelUserPwd = Label(frameUserPwd,text = 'PASSWORD:')
        self.__userPwd = StringVar()
        entryUserPwd = Entry(frameUserPwd,textvariable = self.__userPwd)
        labelUserPwd.pack(side = LEFT)
        entryUserPwd.pack(side = RIGHT)

        labelBlank3 = Label(self.__root)
        labelBlank3.pack(side = TOP)

        frameButton = Frame(self.__root)
        frameButton.pack(side = TOP)
        buttonConfirm = Button(frameButton,text = 'COMFIRM',command = self.sendOutInput)
        buttonCancle = Button(frameButton,text = 'CANCLE',command = self.__root.quit)
        buttonConfirm.pack(side = LEFT)
        buttonCancle.pack(side = RIGHT)

        mainloop()

    def getInput(self):
        login = [self.__userNumber.get(),self.__userPwd.get()]
        return login

    def sendOutInput(self):
        self.__fGet.setLogin(self.getInput())
        self.__root.quit()
        return

class C_GetLogin():
    def __init__(self):
        self.__logKey = ['','']


    def setLogin(self,logKey):
        self.__logKey = logKey

    def getLogin(self):
        v = V_login(self)
        return self.__logKey

c = C_GetLogin()
print(c.getLogin())