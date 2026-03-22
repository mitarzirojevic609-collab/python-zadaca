import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='12061998',
    database='python17'
)
if connection.open:
    print('konekcija je uspostavljena')
else:
    print('konekcija nije uspostavljena')


def create_user(con, username, password, age):
    cursor = con.cursor()
    query = "INSERT INTO users (username, password, age) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, password, age))
    con.commit()
    cursor.close()
create_user(connection, "nevena", "luiviton", 22)

