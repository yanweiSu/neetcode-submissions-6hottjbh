class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        # search on timestamp:
        data = self.data[key].copy()
        left, right = 0, len(data) - 1
        # number of elements that are leq than timestamp
        retidx = -1
        while left <= right:
            mid = (left + right) // 2
            if data[mid][0] > timestamp:
                right = mid - 1
            if data[mid][0] <= timestamp:
                # might be the solution
                retidx = mid
                left = mid + 1

        if retidx >= 0 and data[retidx][0] <= timestamp:
            return data[retidx][1]
        return ""
        
