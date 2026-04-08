class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while(start <= end):
            i = (start + end) // 2
            if nums[i] == target:
                return i

            if target < nums[i]:
                end = i - 1
            else:
                start = i + 1
        
        return -1