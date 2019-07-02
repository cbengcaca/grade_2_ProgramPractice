from tkinter import *
class V_getIsbn:
    def __init__(self,fGet):
        self.fGet = fGet
        self.root = Toplevel()
        self.root.title('LOGIN')
        self.root.resizable(0, 0)
        self.root.geometry('400x200')
        labelBlank = Label(self.root)
        labelBlank.pack(side = TOP)
        frameTop = Frame(self.root)
        frameTop.pack(side = TOP)

        self.isbnVar = StringVar()
        labelIsbn = Label(frameTop,text = 'Input isbn :')
        labelIsbn.pack(side = LEFT)
        EntryIsbn = Entry(frameTop , textvariable = self.isbnVar)
        EntryIsbn.pack(side = LEFT)

        labelBlank2 = Label(self.root)
        labelBlank2.pack(side = TOP)
        frameBottom = Frame(self.root)
        frameBottom.pack(side = TOP)

        buttonConfirm = Button(frameBottom, text='CONFIRM',command = self.sendOutInput)
        buttonConfirm.pack(side = LEFT)
        buttonCancle = Button(frameBottom,text = 'CANCLE')
        buttonCancle.pack(side = LEFT)

        mainloop()

    def sendOutInput(self):
        self.fGet.setIsbn(self.isbnVar.get())
        self.root.quit()
        self.root.destroy()


