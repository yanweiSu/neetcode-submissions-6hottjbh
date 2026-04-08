class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxpile = -float("inf")
        for p in piles:
            if p > maxpile:
                maxpile = p

        start, end = 1, maxpile
        while (start <= end):
            i = (start + end) // 2
            # compute taken hours
            t = 0
            for p in piles:
                t += math.ceil(p/i)
                if t > h:
                    break
                    
            if t > h:
                # k too small
                start = i + 1
            else:
                # end is valid
                end = i

            if (start == end):
                return start

            
