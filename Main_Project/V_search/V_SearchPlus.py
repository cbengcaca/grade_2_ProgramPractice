from tkinter import *

class V_SearchPlus():
    def __init__(self,father):
        self.root = Toplevel(father)
        self.root.title('SEARCHPLUS')
        self.root.geometry('400x300')
        self.root.resizable(0,0)
        self.root.attributes("-toolwindow", 1)
        self.root.wm_attributes("-topmost", 1)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        labelInputTip = Label(self.root,text = 'INPUT HERE:')
        labelInputTip.pack(side = TOP)

        labelRule1 = Label(self.root,text = 'RULE1')
        labelRule1.pack(side = TOP)
        entryInput1 = Entry(self.root)
        entryInput1.pack(side = TOP)

        labelRule2 = Label(self.root,text = 'RULE2')
        labelRule2.pack(side = TOP)
        entryInput2 = Entry(self.root)
        entryInput2.pack(side = TOP)

        labelRule3 = Label(self.root,text = 'RULE3')
        labelRule3.pack(side = TOP)
        entryInput3 = Entry(self.root)
        entryInput3.pack(side = TOP)

        labelBlank2 = Label(self.root)
        labelBlank2.pack(side = TOP)
        
        frameOkCancle = Frame(self.root)
        frameOkCancle.pack(side = TOP)

        buttonConfirm = Button(frameOkCancle,text = 'CONFIRM')
        buttonConfirm.pack(side = LEFT)
        buttonCancle = Button(frameOkCancle,text = 'CANCLE')
        buttonCancle.pack(side = RIGHT)

        mainloop()