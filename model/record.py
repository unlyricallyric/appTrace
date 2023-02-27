import json


class Record:
    def __init__(self, record):
        self.record = record
        self.data = json.loads(self.get_data())
        self.id = record[0]
        self.action = self.get_action()
        self.duration = self.get_duration()
        self.last_operation = self.get_last_operation()

    def get_id(self):
        return self.record[0]

    def get_duration(self):
        return int(self.record[2]) - int(self.record[1])

    def get_data(self):
        return self.record[3]

    def get_action(self):
        return self.data['action']

    def get_last_operation(self):
        navigation_history = self.data['navigation_history']
        return navigation_history[len(navigation_history) - 1]
