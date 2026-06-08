class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        return self.subsets(nums[1:]) + [[nums[0]] + x for x in self.subsets(nums[1:])]