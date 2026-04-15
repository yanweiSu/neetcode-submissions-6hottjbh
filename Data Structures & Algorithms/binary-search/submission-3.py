class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 搜尋範圍，包含 start & end element
        start, end = 0, len(nums) - 1

        while(start <= end):
            i = (start + end) // 2
            if nums[i] == target:
                return i

            if target < nums[i]:
                end = i - 1
            else: # target > nums[i]
                start = i + 1
        
        return -1