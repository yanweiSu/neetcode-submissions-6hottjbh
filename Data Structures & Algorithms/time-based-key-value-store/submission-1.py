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
        while (left < right):
            mid = (left + right) // 2
            if data[mid][0] > timestamp:
                right = mid - 1
            if data[mid][0] < timestamp:
                if data[mid + 1][0] <= timestamp:
                    left = mid + 1
                else:
                    return data[mid][1]
            if data[mid][0] == timestamp:
                return data[mid][1]

        if data[left][0] > timestamp:
            return ""
        return data[left][1]
        
