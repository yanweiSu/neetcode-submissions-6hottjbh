class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if not nums:
            return [[]]
        
        for _ in range(len(nums)):
            fixed = nums.pop()
            perms = self.permute(nums)
            perms = [perm + [fixed] for perm in perms]
            result.extend(perms)
            
            # nums = [fixed] + nums
            nums.insert(0, fixed)

        return result