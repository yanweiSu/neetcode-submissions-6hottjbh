class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles) + 1
        # [lo, hi)
        while (lo < hi):
            mid = (lo + hi) // 2    # mid < hi when lo < hi

            valid = True
            s = 0
            for p in piles:
                s += math.ceil(p / mid)
                if s > h:
                    valid = False
                    break

            if valid:
                hi = mid
            else:
                lo = mid + 1

        return lo


