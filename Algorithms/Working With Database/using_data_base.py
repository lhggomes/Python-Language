import psycopg2 as pdb

config = dict(hostname="localhost",
              username="root",
              password="1234",
              database="computer_vision",
              table="usuarios",
              port="5432")


class Connector:
    def __init__(self, **kwargs):
        self._database = kwargs.pop('database', config['database'])
        self._user = kwargs.pop('username', config['username'])
        self._host = kwargs.pop('hostname', config['hostname'])
        self._password = kwargs.pop('password', config['password'])
        self._port = kwargs.pop('port', config['port'])
        self._table = kwargs.pop('table', config['table'])
        self._user_id = None

        try:
            self._connection = pdb.connect(database=self._database, user=self._user, password=self._password,
                                           host=self._host, port=self._port)
            self._create_cursor()

        except:
            print('Impossible to connect')
            # Implement a Custom Execpetion

    def _create_cursor(self):
        self._cursor = self._connection.cursor()

    def sql_search_find_all(self):
        sql = "SELECT * FROM %s" % self._table
        self._cursor.execute(sql)
        rows = self._cursor.fetchall()

    def sql_search_find_by_id(self, user_id):
        self._user_id = user_id
        sql = "SELECT * FROM {} WHERE id= '{}'".format(self._table, self._user_id)

        self._cursor.execute(sql)
        row = self._cursor.fetchone()
        users = []
        for i in row:
            users.append(i)

        return users
