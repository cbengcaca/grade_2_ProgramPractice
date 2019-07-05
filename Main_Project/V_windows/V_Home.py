from tkinter import *
from V_windows.V_search.V_SearchMain import V_Search
from V_windows.V_readerEntrance.V_ReaderEntrance import V_ReaderEntrance
from V_windows.V_adminEntrance.V_AdminEntrance import V_AdminEntrance

class V_Home():
    def __init__(self):
        self.size = '450x250'
        self.locate = '+10+10'
        self.root = Tk()
        self.root.title('主页')
        self.root.geometry(self.size)
        self.root.geometry(self.locate)
        self.root.resizable(0,0)


        labelBlank1 = Label(self.root)
        labelBlank1.pack(side = TOP)

        buttonSearch = Button(self.root,text = '查询书籍',command = self.openSearchEntrance,font = 'Consoles')
        buttonSearch.pack(side = TOP)

        labelBlank2 = Label(self.root)
        labelBlank2.pack(side = TOP)

        buttonReader = Button(self.root,text = '读者入口',command = self.openReaderWindow,font = 'Consoles')
        buttonReader.pack(side = TOP)

        labelBlank3 = Label(self.root)
        labelBlank3.pack(side = TOP)

        buttonAdmin = Button(self.root,text = '管理员入口',command = self.openAdminWindow,font = 'Consoles')
        buttonAdmin.pack(side = TOP)

        labelBlankLast = Label(self.root)
        labelBlankLast.pack(side = TOP)

        buttonClose = Button(self.root,text = '关闭本系统', command = self.root.destroy, font = 'Consoles')
        buttonClose.pack(side = TOP)

        mainloop()


    def openSearchEntrance(self):
        searchEntrance = V_Search()
        return

    def openReaderWindow(self):
        readerEntrance = V_ReaderEntrance()
        return

    def openAdminWindow(self):
        adminEntrance = V_AdminEntrance()
        return



a = V_Home()