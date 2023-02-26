import queue
import sqlite3

from connection_pool.connection_pool import ConnectionPool


class SqliteConnectionPool(ConnectionPool):
    def __init__(self, database_path, max_connections):
        self.max_connections = max_connections
        self.sqlite_pool = queue.Queue(maxsize=max_connections)

        for i in range(max_connections):
            conn = sqlite3.connect(database_path)
            self.sqlite_pool.put(conn)

    def acquire(self):
        return self.sqlite_pool.get()

    def release(self, conn):
        return self.sqlite_pool.put(conn)

    def close_all(self):
        while not self.sqlite_pool.empty():
            conn = self.sqlite_pool.get()
            conn.close()
