from tkinter import *
import tkinter.messagebox
class V_DownBook():

    def __init__(self,father):
        self.father = father
        self.root = Tk()
        self.root.title('DownBook')
        self.root.geometry('400x200')
        self.root.geometry(self.father.locate)
        self.root.resizable(0,0)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        labelInputTip = Label(self.root,text = 'Input Here:')
        labelInputTip.pack(side = TOP)

        labelBookNumber = Label(self.root,text = 'BookNumber:')
        labelBookNumber.pack(side = TOP)
        entryInput2 = Entry(self.root)
        entryInput2.pack(side = TOP)

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
        tkinter.messagebox.showinfo('提示', '下架成功')

    def returnFather(self):
        self.father.showThisWindow()
        self.root.destroy()