import pymysql
import sys
import abc


class connection:
    def create_connection(self, host="localhost", user="root", password="", data_base="", port=3306):
        global con
        global status

        try:
            con = pymysql.connect(
                host,
                user,
                password,
                data_base,
                port
                )
            status = True
        except:
            print('Erro não foi possível Connectar', sys.exc_info()[0])
            status = False

        return con

    @abc.abstractstaticmethod
    def is_connect(self):
        global status
        if status :
            return True
        else :
            return False
