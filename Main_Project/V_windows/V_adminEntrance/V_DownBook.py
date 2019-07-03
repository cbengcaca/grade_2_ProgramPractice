from tkinter import *
from tkinter import messagebox
from VC_windowsControl.VC_downBook import VC_downBook
class V_DownBook():

    def __init__(self,operId):
        self.operId = operId
        self.root = Toplevel()
        self.root.title('DownBook')
        self.root.geometry('400x200')
        self.root.resizable(0,0)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        labelInputTip = Label(self.root,text = '请输入要下架的书籍Id:')
        labelInputTip.pack(side = TOP)

        self.bookId = StringVar()
        entryBookId = Entry(self.root,textvariable = self.bookId)
        entryBookId.pack(side = TOP)


        buttonConfirm = Button(self.root,text = '确认',command = self.getInput)
        buttonConfirm.pack(side = TOP)

        buttonReturn = Button(self.root, text='返回', command=self.returnFather, font='Consoles')
        buttonReturn.pack(side=BOTTOM)

        mainloop()


    def getInput(self):
        infoList = ['5']
        infoList.append(self.bookId.get())
        infoList.append(self.operId)
        infoList.append('==')
        vc = VC_downBook()
        sign = vc.deleteBook(infoList)
        if sign[0][0] is '1':
            messagebox.showinfo(message='下架成功')
        else:
            messagebox.showerror(message='下架失败')

    def returnFather(self):
        self.root.quit()
        self.root.destroy()

# a = V_DownBook('2')
# getInput = a.getInput()



