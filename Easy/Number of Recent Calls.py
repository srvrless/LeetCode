import heapq


class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        heapq.heapify(self.queue)
        while self.queue and self.queue[0] + 3000 < t:
            heapq.heappop(self.queue)
        heapq.heappush(self.queue, t)
        return len(self.queue)