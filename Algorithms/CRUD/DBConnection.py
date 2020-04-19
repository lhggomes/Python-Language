import pymysql
import sys


def is_connect():
    global status
    if status :
        return True
    else:
        return False


class connection:

    def create_connection(self, host="localhost", user="root", password="", data_base="", port=3306):

        self._host = host
        self._user = user
        self._password = password
        self._data_base = data_base
        self._port = port

        global con
        global status

        try :
            con = pymysql.connect(
                self._host,
                self._user,
                self._password,
                self._data_base,
                self._port
                )
            status = True
        except :
            print('Erro não foi possível Connectar', sys.exc_info()[0])
            status = False

        return con
