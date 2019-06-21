import pymysql

class M_DBOperation:
    def __init__(self, infoList):
        self.__bookName = infoList[0]           #书名
        self.__bookMinPrice = infoList[1]       #价格底线
        self.__bookMaxPrice = infoList[2]       #价格上限
        self.__publishTime = infoList[3]        #出版时间
        self.__bookAuthor = infoList[4]         #作者
        self.__bookPublisher = infoList[5]      #出版社
        self.__sortKey = infoList[6]            #排序关键字
        self.__sortFlag = infoList[7]           #升降序标志
        self.__selSQL =  "SELECT bookName, bookPrice, bookCreateTime, bookAuthor, bookPublisher, bookSaleNumber, shelfLocate"
        self.__selSQL += " FROM T_ISBNInfo, T_ISBNAndShelf, T_shelfLocate"
        self.__selSQL += " WHERE T_ISBNInfo.ISBN =  T_ISBNAndShelf.ISBN AND T_shelfLocate.shelfId = T_ISBNAndShelf.shelfId AND T_ISBNInfo.bookMaxNum != 0"

        self.createSQL()
    #连接数据库
    def connectDB(self):
        db = pymysql.connect('localhost','root','19990418sY','softwarepractice')
        return db

    #根据排序关键字和标识符，生成对应的SQL语句
    def createSQL(self):
        # 查找书名、价格、出版时间、作者、出版社、销量、位置
        if self.__bookName != 'None':                                                #书名不为空，模糊查询
            self.__selSQL += " AND bookName LIKE '%" + self.__bookName + "%'"
        if self.__bookMinPrice != 'None':                                            #所查找书籍的价格底线
            self.__selSQL += "AND bookPrice > " + self.__bookMinPrice
        if self.__bookMaxPrice != 'None':                                             #所查找书籍的价格上限
            self.__selSQL += " AND bookPrice < " + self.__bookMaxPrice
        if self.__publishTime != 'None':                                             #出版时间
            self.__selSQL += " AND bookCreateTime =" + self.__publishTime
        if self.__bookAuthor != 'None':                                              #作者不为空，模糊查询
            self.__selSQL += " AND bookAuthor LIKE '%" + self.__bookAuthor + "%'"
        if self.__bookPublisher != 'None':                                           #出版社不为空，模糊查询
           self.__selSQL += " AND bookPublisher LIKE '%" + self.__bookAuthor + "%'"

        if self.__sortKey == "书名":                                               #按书名首字母[汉字拼音首字母]排序
            self.__selSQL += "ORDER BY bookName"
        if self.__sortKey == "价格":                                               #按价格排序
            self.__selSQL += "ORDER BY bookPrice"
        if  self.__sortKey == "销量":                                              #按销量排序
            self.__selSQL += "ORDER BY bookSaleNum"
        if self.__sortFlag == '0':                                                   #降序排列
            self.__selSQL += " DESC"

    #查询书籍并返回书籍信息
    def selectBook(self):
        ret = ''
        con = self.connectDB()
        cursor = con.cursor()
        try:
            cursor.execute(self.__selSQL)
            ret = cursor.fetchall()
            con.close()
        except Exception as e:
            print("error:unable to fetch data", e)
        return ret

if __name__=='__main__':
    L = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
    p = M_DBOperation(L)
    if p.selectBook():
        for singleLine in p.selectBook():
            singleLineChangeToStr = ','.join([str(i) for i in singleLine])
            print(singleLineChangeToStr)