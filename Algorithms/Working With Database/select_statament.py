from Algorithms.CRUD import DBConnection as Db

connect = Db.create_connection(data_base="precos")
cursor_db = connect.cursor()


query = "SELECT * FROM prodmov ORDER BY numtransmov"

if Db.is_connect():
    cursor_db.execute(query)
    result = cursor_db.fetchall()

    for x in result:
        print(x)



