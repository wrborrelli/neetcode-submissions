class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        outs = []
        for i in range(len(nums)-k+1):
            print(nums[i:i+k])
            outs.append(max(nums[i:i+k]))
        return outs