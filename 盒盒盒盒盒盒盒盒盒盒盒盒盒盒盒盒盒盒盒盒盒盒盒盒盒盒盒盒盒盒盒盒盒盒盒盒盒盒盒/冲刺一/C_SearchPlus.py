import huangweisheng

class C_SearchPlus:

    def __init__(self):
        self.host = '10.240.224.173'
        self.bookList = []

    def sendSearchToTcp(self, v_searchPlus, searchList):
        sendToServ = SendToServ()
        sendToServ.send(searchList, self.host, self.bookList)
        self.viewBookInformation(v_searchPlus)

    def viewBookInformation(self,v_searchPlus):
        v_searchPlus.showBookInformation(self.bookList)



