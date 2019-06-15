from tkinter import *
import tkinter.messagebox
class V_DownBook():

    def __init__(self):
        self.__root = Tk()
        self.__root.title('DownBook')
        self.__root.geometry('400x200')
        self.__root.resizable(0,0)

        labelBlank1 = Label(self.__root)
        labelBlank1.pack(side = TOP)

        labelInputTip = Label(self.__root,text = 'Input Here:')
        labelInputTip.pack(side = TOP)

        labelBookNumber = Label(self.__root,text = 'BookNumber:')
        labelBookNumber.pack(side = TOP)
        entryInput2 = Entry(self.__root)
        entryInput2.pack(side = TOP)

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
        tkinter.messagebox.showinfo('提示', '下架成功')


a = V_DownBook()
