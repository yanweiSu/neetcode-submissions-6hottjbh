class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(arr, target):
            if target == 0:
                return [[]]
            if not arr:
                return []
            if target < 0:
                return []

            case1 = helper(arr[1:], target - arr[0])
            idx = 0
            for i in range(len(arr)):
                if arr[i] != arr[0]:
                    idx = i
                    break
            case2 = []
            if idx > 0:
                case2 = helper(arr[idx:], target)

            return [[arr[0]] + x for x in case1] + case2

        return helper(sorted(candidates), target)