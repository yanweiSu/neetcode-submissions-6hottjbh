class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)
        for i in range(1, len(nums)):
            ret[i] = ret[i-1] * nums[i-1]

        right = 1
        for j in range(len(nums)-2, -1, -1):
            right = right * nums[j+1]
            ret[j] *= right

        return ret