from database.database import Database
from database.database_type import DatabaseType
from repository.traceApp_repository import TraceAppRepository

database_params = 'apptrace.db'

# initialize database instance with a max connection
max_connections = 2
db = Database(DatabaseType.sqlite, database_params, max_connections)

# get a connection from pool
conn = db.sqlite_db.acquire()

# initialize repository
appTraceRepo = TraceAppRepository(conn)

# Set a batch size for batch processing
batch_size = 1000
number_of_records = 2

slowest_record_info = appTraceRepo.get_slowest_records_info(batch_size, number_of_records)

# release connection
db.sqlite_db.release(conn)
