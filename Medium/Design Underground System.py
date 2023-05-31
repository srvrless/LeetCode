import collections


class UndergroundSystem:

    def __init__(self):
        self.user = collections.defaultdict(list)
        self.dest = collections.defaultdict(list)

    def checkIn(self, id, stationName, t):
        self.user[id] = [stationName, t]

    def checkOut(self, id, stationName, t):
        start_station, prev_time = self.user[id]
        self.dest[(start_station, stationName)].append(t - prev_time)

    def getAverageTime(self, startStation, endStation):
        return float(sum(self.dest[(startStation, endStation)])) / len(
            self.dest[(startStation, endStation)])
