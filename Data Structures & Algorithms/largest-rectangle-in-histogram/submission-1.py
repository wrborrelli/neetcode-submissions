class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        cmax = max(heights)
        for i in range(len(heights)-1):
            for j in range(i+2,len(heights)+1):
                tmax = len(heights[i:j])*min(heights[i:j])
                if tmax > cmax:
                    cmax = tmax
                else:
                    None
        return cmax
        
        