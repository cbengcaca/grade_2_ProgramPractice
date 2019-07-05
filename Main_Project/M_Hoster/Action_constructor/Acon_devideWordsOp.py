import pymysql

class Acon_devideWordsOp:
    def setSearch(self, infoList):
        self.__bookName = infoList[0]           #书名
        self.__bookMinPrice = infoList[1]       #价格底线
        self.__bookMaxPrice = infoList[2]       #价格上限
        self.__publishTime = infoList[3]        #出版时间
        self.__bookAuthor = infoList[4]         #作者
        self.__bookPublisher = infoList[5]      #出版社
        self.__sortKey = infoList[6]            #排序关键字
        self.__sortFlag = infoList[7]           #升降序标志
        self.__selSQL =  "SELECT DISTINCT a.bookName,a.bookPrice,a.bookCreateTime,a.bookAuthor, " \
                         "a.bookPUblisher,a.bookAvailableNum ,a.bookSaleNumber, a.shelflocate, date_format(b.returntime, '%Y%m%d')"
        self.__selSQL += " from v_isbnlocate a left join v_borrowandbookinfo b on a.isbn = b.isbn "
        #date_format(time, '%Y%m%d')
        flagIfFirst = 0
        previousNum = 0
        # 查找书名、价格、出版时间、作者、出版社、销量、位置
        if self.__bookName != 'None':  # 书名不为空，模糊查询
            flagIfFirst += 1
            previousNum += 1
            if flagIfFirst is 1:
                self.__selSQL += " Where "
            if previousNum >= 2:
                self.__selSQL += " AND "
            self.__selSQL += "bookName LIKE '%" + self.__bookName + "%'"
        if self.__bookMinPrice != 'None':  # 所查找书籍的价格底线
            flagIfFirst += 1
            previousNum += 1
            if flagIfFirst is 1:
                self.__selSQL += " Where "
            if previousNum >= 2:
                self.__selSQL += " AND "
            self.__selSQL += "bookPrice > " + self.__bookMinPrice
        if self.__bookMaxPrice != 'None':  # 所查找书籍的价格上限
            flagIfFirst += 1
            previousNum += 1
            if flagIfFirst is 1:
                self.__selSQL += " Where "
            if previousNum >= 2:
                self.__selSQL += " AND "
            self.__selSQL += "bookPrice < " + self.__bookMaxPrice
        if self.__publishTime != 'None':  # 出版时间
            flagIfFirst += 1
            previousNum += 1
            if flagIfFirst is 1:
                self.__selSQL += " Where "
            if previousNum >= 2:
                self.__selSQL += " AND "
            self.__selSQL += "bookCreateTime =" + self.__publishTime
        if self.__bookAuthor != 'None':  # 作者不为空，模糊查询
            flagIfFirst += 1
            previousNum += 1
            if flagIfFirst is 1:
                self.__selSQL += " Where "
            if previousNum >= 2:
                self.__selSQL += " AND "
            self.__selSQL += "bookAuthor LIKE '%" + self.__bookAuthor + "%'"
        if self.__bookPublisher != 'None':  # 出版社不为空，模糊查询
            flagIfFirst += 1
            previousNum += 1
            if flagIfFirst is 1:
                self.__selSQL += " Where "
            if previousNum >= 2:
                self.__selSQL += " AND "
            self.__selSQL += "bookPublisher LIKE '%" + self.__bookAuthor + "%'"

        if self.__sortKey == "书名":  # 按书名首字母[汉字拼音首字母]排序
            self.__selSQL += " ORDER BY bookName"
        if self.__sortKey == "价格":  # 按价格排序
            self.__selSQL += " ORDER BY bookPrice"
        if self.__sortKey == "销量":  # 按销量排序
            self.__selSQL += " ORDER BY bookSaleNumber"
        if self.__sortFlag == '0':  # 降序排列
            self.__selSQL += " DESC"

        return self.__selSQL
        #根据排序关键字和标识符，生成对应的SQL语句
        #查询书籍并返回书籍信息


L = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
