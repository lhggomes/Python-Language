import pymysql
import sys


def create_connection(host="localhost", user="root", password="", data_base="", port=3306) :
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
        is_connect(True)
    except:
        print('Erro não foi possível Connectar', sys.exc_info()[0])
        is_connect(False)

    return con


def is_connect(status):
    return status

