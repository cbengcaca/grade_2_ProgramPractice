from tkinter import *
import tkinter.messagebox
class V_UpBook():

    def __init__(self):
        self.__root = Tk()
        self.__root.title('UpBook')
        self.__root.geometry('400x400')
        self.__root.resizable(0,0)

        labelBlank1 = Label(self.__root)
        labelBlank1.pack(side = TOP)

        labelInputTip = Label(self.__root,text = 'Input Here:')
        labelInputTip.pack(side = TOP)

        labelBookName = Label(self.__root,text = 'BookName:')
        labelBookName.pack(side = TOP)
        entryInput1 = Entry(self.__root)
        entryInput1.pack(side = TOP)

        labelBookNumber = Label(self.__root,text = 'BookNumber:')
        labelBookNumber.pack(side = TOP)
        entryInput2 = Entry(self.__root)
        entryInput2.pack(side = TOP)

        labelBookAuthor = Label(self.__root,text = 'BookAuthor:')
        labelBookAuthor.pack(side = TOP)
        entryInput3 = Entry(self.__root)
        entryInput3.pack(side = TOP)

        labelBookPublisher = Label(self.__root,text = 'BookPublisher:')
        labelBookPublisher.pack(side = TOP)
        entryInput4 = Entry(self.__root)
        entryInput4.pack(side = TOP)

        labelBookLocation = Label(self.__root,text = 'BookLocation:')
        labelBookLocation.pack(side = TOP)
        entryInput5 = Entry(self.__root)
        entryInput5.pack(side = TOP)

        labelInTime = Label(self.__root,text = 'InTime:')
        labelInTime.pack(side = TOP)
        entryInput6 = Entry(self.__root)
        entryInput6.pack(side = TOP)

        labelBlank2 = Label(self.__root)
        labelBlank2.pack(side = TOP)

        frameOkCancle = Frame(self.__root)
        frameOkCancle.pack(side = TOP)

        buttonConfirm = Button(frameOkCancle,text = 'Confirm',command = self.popup)
        buttonConfirm.pack(side = LEFT)
        buttonCancle = Button(frameOkCancle,text = 'Cancle')
        buttonCancle.pack(side = RIGHT)

        mainloop()

    def popup(self):
        tkinter.messagebox.showinfo('提示', '上架成功')


