from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft() if self.queue else None

    def list_between_dates(self, start_date, end_date):
        return [item for item in self.queue if start_date <= item['date'] <= end_date]
