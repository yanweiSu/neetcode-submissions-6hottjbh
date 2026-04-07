class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-n for n in stones]
        heapq.heapify(arr)
        while(len(arr) > 1):
            max1 = heapq.heappop(arr)
            max2 = arr[0]
            if max1 == max2:
                heapq.heappop(arr)
            else:
                val = max1 - max2 if (max1 < max2) else max2 - max1
                heapq.heapreplace(arr, val)

        if len(arr) == 0:
            return 0
        else:
            return -arr[0]