class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        c1 = 0
        c2 = len(heights)-1
        while c1 < c2:
            t_area = (c2-c1)*min([heights[c1], heights[c2]])
            print(t_area)
            if t_area > max_a:
                max_a = t_area
            else:
                None
            if heights[c1] > heights[c2]:
                c2 -= 1
            else:
                c1 += 1

        return max_a