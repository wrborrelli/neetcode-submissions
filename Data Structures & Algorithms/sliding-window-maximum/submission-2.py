class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        outs = []
        p1=0
        p2=p1+k
        while p2<=len(nums):
            outs.append(max(nums[p1:p2]))
            p1+=1
            p2+=1
        return outs