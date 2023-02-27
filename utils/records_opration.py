def sort_records_by_duration(records, reverse=True):
    return sorted(records, key=lambda x: x.duration, reverse=reverse)


def sort_records_by_id(records, reverse=True):
    return sorted(records, key=lambda x: x.id, reverse=reverse)


def get_app_info_by_records(records):
    for record in records:
        print(record.id, record.duration, record.action, record.last_operation)
