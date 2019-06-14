from tkinter import *
from V_search.V_SearchNormal import V_SearchNormal
from V_search.V_SearchPlus import V_SearchPlus
class V_Search():
    def __init__(self):
        self.root = Tk()
        self.root.title('SEARCH')
        self.root.geometry('400x200')
        self.root.resizable(0,0)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        frameSearchEntrance = Frame(self.root)
        frameSearchEntrance.pack(side = TOP)

        buttonSearchPlus = Button(frameSearchEntrance,text = 'SEARCHPLUS',command = self.openSearchPlus)
        buttonSearchPlus.pack(side = LEFT)

        buttonSearchNormal = Button(frameSearchEntrance,text = 'SEARCHNORMAL',command = self.openSearchNormal)
        buttonSearchNormal.pack(side = RIGHT)

        mainloop()

    def openSearchPlus(self):
        V_searchPlusNew = V_SearchPlus()
        return

    def openSearchNormal(self):
        V_searchNormalNew = V_SearchNormal()
        return

