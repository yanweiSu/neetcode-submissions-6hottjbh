class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rec = {}
        for x in nums:
            if x not in rec:
                rec[x] = 1
            else:
                rec[x] += 1
                
        rec = sorted(rec.items(), key=lambda x: x[1], reverse=True)
        return [key for key, val in rec[:k]]