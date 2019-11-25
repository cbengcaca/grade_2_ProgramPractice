import pymysql
class M_SqlRunner:
    def beginSql(self,sqlList):
        ret = ''
        db = pymysql.connect('106.52.87.149', 'root', '000000', 'softwarePractice')
        cursor = db.cursor()
        try:

            for sql in sqlList:
                tmp = sql.strip(' ').split()[0]
                cursor.execute(sql)
                if tmp == 'SELECT':
                    db.commit()
                    ret = cursor.fetchall()
                    return ret
            db.commit()
            db.close()
            return '0'
        except Exception as e:
            db.rollback()
            print("error:unable to fetch data", e)
            return '-1'

