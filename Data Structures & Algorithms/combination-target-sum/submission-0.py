class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        if target < 0:
            return []
        if target == 0:
            return [[]]

        case1 = self.combinationSum(nums, target - nums[0])
        case2 = self.combinationSum(nums[1:], target)
        return [[nums[0]] + x for x in case1] + case2

