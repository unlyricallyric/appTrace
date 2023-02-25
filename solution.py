import sqlite3

from TraceAppRepository import TraceAppRepository
from database import Database

conn = sqlite3.connect('apptrace.db')

db = Database(TraceAppRepository)

appTraceRepo = TraceAppRepository(conn)

batch_size = 3

max_value = appTraceRepo.batch_get_slowest_app(batch_size)

print(max_value)