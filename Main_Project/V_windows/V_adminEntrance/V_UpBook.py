from tkinter import *
import tkinter.messagebox
class V_UpBook():

    def __init__(self,father):
        self.father = father
        self.root = Tk()
        self.root.title('UpBook')
        self.root.geometry('400x500')
        self.root.geometry(self.father.locate)
        self.root.resizable(0,0)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        labelInputTip = Label(self.root,text = 'Input Here:')
        labelInputTip.pack(side = TOP)

        labelBookName = Label(self.root,text = 'BookName:')
        labelBookName.pack(side = TOP)
        entryInput1 = Entry(self.root)
        entryInput1.pack(side = TOP)

        labelBookNumber = Label(self.root,text = 'BookNumber:')
        labelBookNumber.pack(side = TOP)
        entryInput2 = Entry(self.root)
        entryInput2.pack(side = TOP)

        labelBookAuthor = Label(self.root,text = 'BookAuthor:')
        labelBookAuthor.pack(side = TOP)
        entryInput3 = Entry(self.root)
        entryInput3.pack(side = TOP)

        labelBookPublisher = Label(self.root,text = 'BookPublisher:')
        labelBookPublisher.pack(side = TOP)
        entryInput4 = Entry(self.root)
        entryInput4.pack(side = TOP)

        labelBookLocation = Label(self.root,text = 'BookLocation:')
        labelBookLocation.pack(side = TOP)
        entryInput5 = Entry(self.root)
        entryInput5.pack(side = TOP)

        labelInTime = Label(self.root,text = 'InTime:')
        labelInTime.pack(side = TOP)
        entryInput6 = Entry(self.root)
        entryInput6.pack(side = TOP)

        labelBlank2 = Label(self.root)
        labelBlank2.pack(side = TOP)

        frameOkCancle = Frame(self.root)
        frameOkCancle.pack(side = TOP)

        buttonConfirm = Button(frameOkCancle,text = 'Confirm',command = self.popup)
        buttonConfirm.pack(side = LEFT)
        buttonCancle = Button(frameOkCancle,text = 'Cancle')
        buttonCancle.pack(side = RIGHT)

        labelBlankLast = Label(self.root)
        labelBlankLast.pack(side=BOTTOM)

        buttonReturn = Button(self.root, text='RETURN', command=self.returnFather, font='Consoles')
        buttonReturn.pack(side=BOTTOM)

        mainloop()

    def popup(self):
        tkinter.messagebox.showinfo('提示', '上架成功')

    def returnFather(self):
        self.father.showThisWindow()
        self.root.destroy()
