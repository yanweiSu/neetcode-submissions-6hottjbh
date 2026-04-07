class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        query = [(math.sqrt(x[0]**2 + x[1]**2), x) for x in points]
        heapq.heapify(query)
        ret = []
        for i in range(k):
            minpt = query[0]
            ret.append(minpt[1])

            heapq.heappop(query)

        return ret