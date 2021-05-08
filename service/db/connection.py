from pymysql import connect, cursors
from config.config import DATABASE_CONF


class Connection:
    def __init__(self, __DATABASE_CONF):
        self.conn = connect(**__DATABASE_CONF)
        self.cur = self.conn.cursor(cursors.DictCursor)

    def execute(self, query, args=None):
        return self.cur.execute(query, args)

    def fetchAll(self):
        return self.cur.fetchall()

    def fetchOne(self):
        return self.cur.fetchone()

    def lastId(self):
        return self.cur.lastrowid

    def commit(self):
        print('commit')

        r = self.conn.commit()
        poor.append(self)
        return r

    def rollback(self):
        print('rollback')
        r = self.conn.rollback()
        poor.append(self)
        return r

    def ping(self, reconnect=True):
        return self.conn.ping(reconnect=reconnect)

    def back(self):
        return poor.append(self)


#


class Pool:
    def __init__(self, __DATABASE_CONF):
        self.index = 0
        self.connectPoor = [Connection(__DATABASE_CONF) for i in range(20)]
        self.maxLength = len(self.connectPoor)

    def getConnect(self):
        r = self.connectPoor.pop()
        r.ping()
        return r

    def append(self, conn):
        self.connectPoor.append(conn)


poor = Pool(DATABASE_CONF)
