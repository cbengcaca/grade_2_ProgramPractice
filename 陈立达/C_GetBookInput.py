from tkinter import *

class V_GetBookInput:

    def __init__(self,fGet):
        self.__fGet = fGet
        self.__root = Tk()
        self.__root.title('GetBookInput')
        self.__root.geometry('400x120')
        self.__root.resizable(0,0)

        frameLine = Frame(self.__root)
        labelBlank = Label(self.__root)
        labelBlank.pack(side = TOP)
        frameLine.pack(side = TOP,ipadx = 20)

        labelBookNumber = Label(frameLine,text = 'BOOKNUMBER:')
        self.__stringVarBookNumber = StringVar()
        entryBookNumber = Entry(frameLine,textvariable = self.__stringVarBookNumber)
        labelBookNumber.pack(side = LEFT)
        entryBookNumber.pack(side = RIGHT)

        frameButton = Frame(self.__root)
        labelBlank2 = Label(self.__root)
        labelBlank2.pack()
        frameButton.pack()
        buttonConfirm = Button(frameButton, text = 'Confirm',command = self.sendOutInput)
        buttonCancel = Button(frameButton, text = 'Cancel',command = self.__root.quit)
        buttonConfirm.pack(side = LEFT)
        buttonCancel.pack(side = RIGHT)
        mainloop()

    def getInput(self):
        return self.__stringVarBookNumber.get()

    def sendOutInput(self):
        self.__fGet.setInputLine(self.getInput())
        self.__root.quit()
        return

class C_GetBookInput():
    def __init__(self):
        self.__inputLine = ''

    def setInputLine(self,str):
        self.__inputLine = str

    def getBookInput(self):
        v = V_GetBookInput(self)
        return self.__inputLine

a = C_GetBookInput()
print(a.getBookInput())


