class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        c0 = 0
        c1 = len(nums)-1
        if nums[c0] > nums[c1]:
            current = nums[c1]
            while current > nums[c1 - 1]:
                c1 -= 1
                current = nums[c1]
            return current
        else:
            current = nums[c0]
            while current > nums[c0 + 1]:
                c0 += 1
                current = nums[c0]
            return current