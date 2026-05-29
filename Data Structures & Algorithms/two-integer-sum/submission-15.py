class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c1 = 0
        c2 = len(nums)-1
        usnum = nums.copy()
        nums.sort()
        while c1 < c2:
            tsum = nums[c1] + nums[c2]
            if tsum == target:
                out = []
                for j in range(len(usnum)):
                    if usnum[j] == nums[c1]:
                        out.append(j)
                    elif usnum[j] == nums[c2]:
                        out.append(j)
                    else:
                        None
                out = list(set(out))
                out.sort()
                return out
            elif tsum < target:
                c1 += 1
            elif tsum > target:
                c2 -= 1
            else:
                None
    
            