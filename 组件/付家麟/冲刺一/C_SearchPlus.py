from sendToServ import *

class C_SearchPlus:

    def __init__(self):
        self.host = '192.168.43.125'
        self.bookList = []

    def sendSearchToTcp(self, v_searchPlus, searchList):
        sendToServ = SendToServ()
        self.bookList = sendToServ.send(searchList, self.host)
        self.viewBookInformation(v_searchPlus)

    def viewBookInformation(self,v_searchPlus):
        v_searchPlus.setBookInformation(self.bookList)



