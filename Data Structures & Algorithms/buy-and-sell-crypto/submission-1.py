class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0 
        for i in range(len(prices)-1):
            bp = max(prices[i+1:]) - prices[i]
            if bp > max_prof:
                max_prof = bp
            else:
                None
        return max_prof