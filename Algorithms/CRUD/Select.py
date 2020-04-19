from Algorithms.CRUD import DBConnection

connect = DBConnection.connection(data_base='precos')
c = connect.create_cursor()

query = "SELECT * FROM prodmov ORDER BY numtransmov"

if connect.is_connect():
    c.execute(query)
    result = c.fetchall()

    for x in result:
        print(x)



