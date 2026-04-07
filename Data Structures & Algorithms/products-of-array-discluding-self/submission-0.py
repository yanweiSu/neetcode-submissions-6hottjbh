class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [nums[0]] * len(nums)
        suffix_prod = [nums[-1]] * len(nums)
        for i in range(1, len(nums)):
            prefix_prod[i] = prefix_prod[i-1] * nums[i]
        for j in range(len(nums)-2, -1, -1):
            suffix_prod[j] = suffix_prod[j+1] * nums[j]

        ret = []
        for i in range(len(nums)):
            ans = 1
            if i > 0:
                ans *= prefix_prod[i-1]
            if i < len(nums) - 1:
                ans *= suffix_prod[i+1]

            ret.append(ans)

        return ret
