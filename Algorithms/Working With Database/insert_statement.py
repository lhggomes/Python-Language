from Algorithms.CRUD import DBConnection as Db
import sys

connection = Db.create_connection(data_base="precos")
c = connection.cursor()

sql = "INSERT INTO prodmov (numtransmov, codprod, qt, precoCompra, numnfent, codfornec) VALUES (4, 10104, 1423, 1, 1, " \
      "124, 3352) "

try:
    c.execute(sql)
    connection.commit()
except:
    print('Erro não foi possivel inserir', sys.exc_info()[0])
    connection.rollback()
finally:
    c.close()
    print("Connection Closed")



