import math

def rate_works(piles, rate, h):
        ttime = 0
        for p in piles:
            ttime += math.ceil(p/rate)
        return ttime <= h

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
    
        while left < right:
            mid = (left + right) // 2
            # Check if mid speed works
            if sum((p + mid - 1) // mid for p in piles) <= h:
                right = mid # Try smaller
            else:
                left = mid + 1 # Need faster
        return left
        