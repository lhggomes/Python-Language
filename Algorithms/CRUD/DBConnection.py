import pymysql
import sys


class connection :
    def __init__(self, host='localhost', user='root', password='', data_base='', port='3306', charset='utf8mb4') :
        self._host = host
        self._user = user
        self._password = password
        self._data_base = data_base
        self._port = port
        self._charset = charset

        global con
        try :
            con = pymysql.connect(
                self._host,
                self._password,
                self._data_base,
                self._port,
                self._charset)

        except :
            print('Erro não foi possível Connectar', sys.exc_info()[0])

    def is_connect(self) :
        global con
        if self.con is not None :
            return True
        else :
            return False
