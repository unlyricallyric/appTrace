from model.record import Record
from priority_queue.priority_queue import PriorityQueue
from repository.repository import Repository
from utils.records_opration import sort_records_by_duration, get_app_info_by_records


class TraceAppRepository(Repository):
    def get_slowest_records_info(self, batch_size, number_of_records):
        record_ids = self.get_slowest_records_ids(batch_size, number_of_records)
        records = self.get_records_by_ids(record_ids)
        records = sort_records_by_duration(records)
        get_app_info_by_records(records)

    def get_records_by_ids(self, id_list):
        query = f"SELECT * FROM apptrace WHERE id IN ({','.join(map(str, id_list))})"
        rows = self.cursor.execute(query).fetchall()
        records = []
        for row in rows:
            records.append(Record(row))

        return records

    def get_slowest_records_ids(self, batch_size, number_of_records):
        pq = PriorityQueue(max_size=number_of_records)
        total_records_count = self.get_records_count()
        total_batch = int(total_records_count / batch_size) + 1
        for i in range(total_batch):
            offset = i * batch_size
            query = f'' \
                    f'SELECT id, (endTimestamp - startTimestamp) as duration FROM ( ' \
                    f'SELECT id, endTimestamp, startTimestamp FROM apptrace LIMIT {batch_size} OFFSET {offset}' \
                    f') ORDER BY duration DESC LIMIT {number_of_records}'
            rows = self.cursor.execute(query).fetchall()
            for row in rows:
                if pq.size() < number_of_records:
                    pq.add(row[0], row[1])
                else:
                    if row[1] > pq.get_items()[0][1]:
                        pq.add(row[0], row[1])

            processedCount = offset + batch_size if (offset + batch_size) < total_records_count else total_records_count
            # print(f'Processed {processedCount} records out of {total_records_count}')
            if processedCount >= total_records_count:
                break

        items = pq.get_items()
        ids = [item[0] for item in items]
        return ids


