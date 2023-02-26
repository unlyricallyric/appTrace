# import heapq
#
#
# class PriorityQueue:
#     def __init__(self, max_size=10):
#         self.max_size = max_size
#         self.queue = []
#
#     def add(self, item):
#         if len(self.queue) >= self.max_size:
#             heapq.heappushpop(self.queue, item)
#         else:
#             heapq.heappush(self.queue, item)
#
#     def get_items(self):
#         return sorted(self.queue)

import queue


class PriorityQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = queue.PriorityQueue()

    def add(self, id, value):
        if self.queue.qsize() < self.max_size:
            self.queue.put((value, id))
        else:
            smallest_value, smallest_id = self.queue.get()
            if value > smallest_value:
                self.queue.put((value, id))
            else:
                self.queue.put((smallest_value, smallest_id))

    def get_items(self):
        return [(id, value) for value, id in list(self.queue.queue)]

    def size(self):
        return self.queue.qsize()
