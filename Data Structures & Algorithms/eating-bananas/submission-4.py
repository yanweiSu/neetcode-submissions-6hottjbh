class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxpiles = -float("inf")
        for p in piles:
            if p > maxpiles:
                maxpiles = p

        start, end = 1, maxpiles
        while (start < end):
            i = (start + end) // 2
            # Thus start <= i < end

            # compute the taken hours
            t = 0
            for p in piles:
                t += math.ceil(p/i)
                if t > h:
                    break
                    
            if t > h:
                # k too small
                start = i + 1
                # Thus new start <= end
            else:
                # end is valid
                end = i
                # Thus start <= new end
                
        return start
