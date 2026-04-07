class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     ret = [1] * len(nums)
    #     for i in range(1, len(nums)):
    #         ret[i] = ret[i-1] * nums[i-1]

    #     right = 1
    #     for j in range(len(nums)-2, -1, -1):
    #         right = right * nums[j+1]
    #         ret[j] *= right

    #     return ret

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [1] * n
        left, right = 1, 1
        for i in range(1, n):
            left *= nums[i-1] # to i
            right *= nums[n-1-i+1] # to n-i-1
            ret[i] *= left
            ret[n-1-i] *= right

        return ret