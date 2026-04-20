import pymysql
class Db:
    def __init__(self):

          self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="12061998",
            database="bank",

        )
          self.cursor = self.connection.cursor()
          