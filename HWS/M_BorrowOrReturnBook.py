from dbtest import *
class M_BorrowOrReturnBook:
    def borrow(self,UserID,bookID):
        sql = "Select ISBN from t_bookinfo where bookId = '"+bookID+"'"
        db = DBO("106.52.87.149", "root", "000000", "softwarePractice")
        result = db.Search(sql)
        isbn = result[0][0]
        sql = "Updata t_isbninfo set  where ISBN = '"+