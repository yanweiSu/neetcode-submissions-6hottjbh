class Solution:
    def findMin(self, nums: List[int]) -> int:
        # mid < right => break point at ,mid]
        # mid > right => break point at (mid, 
        left, right = 0, len(nums) - 1
        while(left != right):
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
                continue
            if nums[mid] > nums[right]:
                left = mid + 1
                

        return nums[left]