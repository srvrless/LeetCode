import bisect


class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        start_index = bisect.bisect_right(self.events, start)

        # start point must have even index
        if start_index % 2 != 0: return False

        end_index = bisect.bisect_left(self.events, end)

        # Both start and end must have same index before insertion
        if end_index != start_index: return False

        bisect.insort_right(self.events, start)
        bisect.insort_left(self.events, end)
        return True