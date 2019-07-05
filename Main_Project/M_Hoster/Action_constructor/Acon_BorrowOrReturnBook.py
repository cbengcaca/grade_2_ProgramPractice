import time,datetime
def select_isbn(bookID):
    sql = "SELECT ISBN from t_bookinfo where bookId = '" + bookID + "'"
    return sql

def update_num(isbn):
    sql = "Update t_isbninfo set bookAvailableNum = bookAvailableNum-1 where ISBN = '" + isbn + "'"
    return sql

def update_borrowlist(borrowId):
    sql = "Update t_borrowlist set returnTime = '" + str(time.strftime('%Y-%m-%d %H:%M:%S')) + "' where borrowId = '" \
          + borrowId + "'"
    return sql

def select_borrowid(bookID):
    sql = "SELECT max(borrowId) from t_borrowlist where bookId = '" + bookID + "' and returntime is Null"
    return sql