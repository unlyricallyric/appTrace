from model.record import Record
from priority_queue import PriorityQueue
from repository.repository import Repository


class TraceAppRepository(Repository):
    def get_slowest_records_info(self, batch_size, number_of_records):
        record_id = self.get_slowest_records_ids(batch_size, number_of_records)
        return self.get_app_info_by_id(record_id)

    def get_app_info_by_id(self, id_list):
        query = f"SELECT * FROM apptrace WHERE id IN ({','.join(map(str, id_list))})"
        rows = self.cursor.execute(query).fetchall()
        for row in rows:
            record = Record(row)
            print(record.id, record.operation_time, record.action, record.last_operation)

    def get_slowest_records_ids(self, batch_size, number_of_records):
        pq = PriorityQueue(max_size=number_of_records)
        total_records_count = self.get_records_count()
        total_batch = int(total_records_count / batch_size) + 1
        for i in range(total_batch):
            offset = i * batch_size
            query = f'' \
                    f'SELECT id, (endTimestamp - startTimestamp) as timeSpent FROM ( ' \
                    f'SELECT id, endTimestamp, startTimestamp FROM apptrace LIMIT {batch_size} OFFSET {offset}' \
                    f') ORDER BY timeSpent DESC LIMIT {number_of_records}'
            rows = self.cursor.execute(query).fetchall()
            for row in rows:
                if pq.size() < number_of_records:
                    pq.add(row[0], row[1])
                else:
                    if row[1] > pq.get_items()[0][1]:
                        pq.add(row[0], row[1])

            # Print progress information
            processedCount = offset + batch_size if (offset + batch_size) < total_records_count else total_records_count

            # print(f'Processed {processedCount} records out of {total_records_count}')
            if processedCount >= total_records_count:
                break

        items = pq.get_items()
        items = sorted(items, key=lambda x: x[1], reverse=True)
        ids = [item[0] for item in items]
        return ids
