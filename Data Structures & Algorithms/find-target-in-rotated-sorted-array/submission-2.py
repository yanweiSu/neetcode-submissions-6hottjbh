class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while (left < right):
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            if nums[mid] < nums[left]:
                # rotated
                if (target > nums[mid]) and (target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid - 1
                continue

            if nums[mid] > nums[right]:
                # rotated
                if (target < nums[mid]) and (target >= nums[left]):
                    right = mid - 1
                else:
                    left = mid + 1
                continue

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        if nums[left] == target:
            return left
        return -1
