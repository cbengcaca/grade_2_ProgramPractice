from tkinter import *
from V_windows.V_search.V_SearchNormal import V_SearchNormal
from V_windows.V_search.V_SearchPlus import V_SearchPlus

class V_Search():
    def __init__(self):
        self.size = '400x200'
        self.locate = '+400+200'
        self.root = Tk()
        self.root.title('查询')
        self.root.geometry(self.size)
        self.root.geometry(self.locate)
        self.root.resizable(0,0)

        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        frameSearchEntrance = Frame(self.root)
        frameSearchEntrance.pack(side = TOP)

        buttonSearchPlus = Button(frameSearchEntrance,text = '高级SQL查询',command = self.openSearchPlus,font = 'Consoles')
        buttonSearchPlus.pack(side = LEFT)

        buttonSearchNormal = Button(frameSearchEntrance,text = '普通查询',command = self.openSearchNormal,font = 'Consoles')
        buttonSearchNormal.pack(side = RIGHT)

        labelBlank2 = Label(self.root)
        labelBlank2.pack(side = BOTTOM)

        buttonReturn = Button(self.root,text = '返回',command = self.returnFather,font = 'Consoles')
        buttonReturn.pack(side = BOTTOM)
        mainloop()


    def openSearchPlus(self):
        V_searchPlusNew = V_SearchNormal()
        return

    def openSearchNormal(self):
        V_searchNormalNew = V_SearchPlus()
        return

    def returnFather(self):
        self.root.quit()
        self.root.destroy()



