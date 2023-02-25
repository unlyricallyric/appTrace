from repository import Repository


class TraceAppRepository(Repository):
    # def __init__(self):
    #     self.total_records_count = self.cursor.execute('SELECT COUNT(*) FROM apptrace')

    def batch_get_slowest_app(self, batch_size):
        max_value = 0
        total_records_count = 10
        total_batch = int(total_records_count / batch_size) + 1
        for i in range(total_batch):
            offset = i * batch_size
            query = f'' \
                    f'SELECT id, MAX(endTimestamp - startTimestamp) as timeSpent FROM ( ' \
                    f'SELECT id, endTimestamp, startTimestamp FROM apptrace LIMIT {batch_size} OFFSET {offset}' \
                    f')'
            row = self.cursor.execute(query).fetchone()
            batch_max = int(row[1])

            # Update the maximum value if necessary
            if batch_max > max_value:
                max_value = batch_max

            # Print progress information
            processedCount = offset + batch_size if (offset + batch_size) < total_records_count else total_records_count
            print(f'Processed {processedCount} records out of {total_records_count}')

        return max_value
