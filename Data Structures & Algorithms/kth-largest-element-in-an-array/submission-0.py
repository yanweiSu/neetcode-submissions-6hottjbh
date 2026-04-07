class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if heap[0] < nums[i]:
                # Into the heap
                heapq.heapreplace(heap, nums[i])
                
        return heap[0]