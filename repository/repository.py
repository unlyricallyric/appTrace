class Repository:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.cursor = db_connection.cursor()

    def get_records_count(self):
        self.cursor.execute('SELECT COUNT(*) FROM apptrace')
        return self.cursor.fetchone()[0]
