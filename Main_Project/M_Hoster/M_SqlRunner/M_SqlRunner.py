import pymysql
class M_SqlRunner:
    def beginSql(self,sql):
        tmp = sql.strip(' ').split()[0]
        ret = ''
        db = pymysql.connect('106.52.87.149', 'root', '000000', 'softwarePractice', autocommit=True)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            if tmp is "select":
                ret = cursor.fetchall()
            else:
                pass
            db.close()
            print("operation done")
        except Exception as e:
            print("error:unable to fetch data", e)

        return ret