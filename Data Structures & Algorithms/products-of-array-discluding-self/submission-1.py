class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            rest = [x for x in range(len(nums)) if x not in [i]]
            tout = 1
            for j in rest:
                tout *= nums[j]
            out.append(tout)
        return out