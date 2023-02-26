from database.database import Database
from database.database_type import DatabaseType
from repository.traceApp_repository import TraceAppRepository

sqlite_params = 'apptrace.db'
db = Database(DatabaseType.sqlite, sqlite_params, 1)
conn = db.sqlite_db.acquire()
appTraceRepo = TraceAppRepository(conn)

batch_size = 3

max_value = appTraceRepo.batch_get_slowest_app(batch_size)

print(max_value)