class Interval:
    def __init__(self, start, end):
        assert start <= end
        self.start, self.end = start, end
    
    def __lt__(self, other):
        assert isinstance(other, Interval)
        if self.end - self.start == other.end - other.start:
            return self.start < other.start
        else:
            return self.end - self.start < other.end - other.start

    def toString(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"
        
def mergeIntervals(intervals):
    result = []
    if len(intervals) > 0:
        # intervals.sort(key = lambda x : x.start)
        intervals.sort()
        for i in intervals:
            if len(result) == 0:
                result.append(i)
            else:
                top = result.pop()
                if top.end >= i.start:
                    newInterval = Interval(top.start, max(top.end, i.end))
                    result.append(newInterval)
                else:
                    result.append(top)
                    result.append(i)
    return result
    
def insertInterval(intervals, newInterval):
    # intervals.sort(key = lambda x : x.start)
    intervals.sort()
    i = 0
    while i < len(intervals) and intervals[i].end < newInterval.start:
        i += 1
    intervals.insert(i, newInterval)
    return mergeIntervals(intervals)