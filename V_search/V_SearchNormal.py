from tkinter import *

class V_SearchNormal():
    def __init__(self):
        self.root = Tk()
        self.root.title('SEARCHNORMAL')
        self.root.geometry('400x200')
        self.root.resizable(0,0)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        labelInputTip = Label(self.root,text = 'INPUT HERE:')
        labelInputTip.pack(side = TOP)

        entryInputSentence = Entry(self.root)
        entryInputSentence.pack(side = TOP)

        frameOkCancle = Frame(self.root)
        frameOkCancle.pack(side = TOP)

        buttonConfirm = Button(frameOkCancle,text = 'CONFIRM')
        buttonConfirm.pack(side = LEFT)
        buttonCancle = Button(frameOkCancle,text = 'CANCLE')
        buttonCancle.pack(side = RIGHT)

        mainloop()
