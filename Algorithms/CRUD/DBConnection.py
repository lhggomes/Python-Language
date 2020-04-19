import pymysql



class connection():
    def __init__(self, host='localhost', user='root', password='', data_base='', port='3306', charset='utf8mb4'):
        self._host = host
        self._user = user
        self._password = password
        self._data_base = data_base
        self._port = port
        self._charset = charset

    @property
    def create_connection(self):
        try:
            con = pymysql.connect(
                self._host,
                self._password,
                self._data_base,
                self._port,
                self._charset )

        except pymysql.connections.err:
            print('Erro não foi possível Connectar')

        finally:
            return con
