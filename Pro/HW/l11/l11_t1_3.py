from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from uuid import uuid4
from datetime import datetime
from datetime import timedelta

auth_provider = PlainTextAuthProvider(username='ALEX', password='x5604')

cluster = Cluster(['127.0.0.1'], auth_provider=auth_provider)
session = cluster.connect()

session.set_keyspace('events_keyspace')

tab_query = """
CREATE TABLE IF NOT EXISTS event_logs (
     event_id UUID PRIMARY KEY,
     user_id UUID,
     event_type TEXT,
     timestamp TIMESTAMP,
     metadata TEXT
);
"""

session.execute(tab_query)

event_id = uuid4()
user_id = uuid4()
event_type = "login"
timestamp = datetime.now()
metadata = '{"ip": "192.168.1.1", "device": "mobile"}'

insert_query = """
INSERT INTO event_logs (event_id, user_id, event_type, timestamp, metadata)
VALUES (%s, %s, %s, %s, %s)
"""
session.execute(insert_query, (event_id, user_id, event_type, timestamp, metadata))

time_24_hours_ago = datetime.now() - timedelta(days=1)
select_query = """
SELECT * FROM event_logs
WHERE event_type = %s AND timestamp > %s
"""
rows = session.execute(select_query, ('login', time_24_hours_ago))

for row in rows:
    print(row.event_id, row.user_id, row.event_type, row.timestamp, row.metadata)

update_query = """
UPDATE event_logs
SET metadata = %s
WHERE event_id = %s
"""
new_metadata = '{"ip": "192.168.1.2", "device": "tablet"}'
event_id_to_update = uuid4()  # замените на реальный event_id

session.execute(update_query, (new_metadata, event_id_to_update))


delete_query = """
DELETE FROM event_logs
WHERE timestamp < %s
"""
time_7_days_ago = datetime.now() - timedelta(days=7)
session.execute(delete_query, (time_7_days_ago,))

cluster.shutdown()

