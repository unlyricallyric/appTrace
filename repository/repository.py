class Repository:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.cursor = db_connection.cursor()

    def batch_get_slowest_app(self, batch_size):
        pass
