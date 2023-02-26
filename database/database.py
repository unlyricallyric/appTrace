from connection_pool.sqlite_connection_pool import SqliteConnectionPool
from database.database_type import DatabaseType


class Database:
    def __init__(self, database_type, database_params, max_connections):
        self.database_type = database_type

        if database_type == DatabaseType.sqlite:
            self.sqlite_db = SqliteConnectionPool(database_params, max_connections)


