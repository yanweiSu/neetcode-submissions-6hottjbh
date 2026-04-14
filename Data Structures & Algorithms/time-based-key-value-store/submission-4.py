from collections import defaultdict
from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.ts = defaultdict(list)
        self.vals = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ts[key].append(timestamp)
        self.vals[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect_right(self.ts[key], timestamp) - 1
        return self.vals[key][idx] if idx >= 0 else ""