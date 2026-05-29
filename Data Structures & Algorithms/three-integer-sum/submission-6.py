class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        c1 = 0
        c2 = len(nums)-1
        cm = c2 - 1
        tl = []
        while c1 < cm < c2:
            while c1 < cm:
                tsum = nums[c1]+nums[cm]+nums[c2]
                if tsum == 0:
                    tl.append([nums[c1],nums[cm],nums[c2]])
                    cm -= 1
                    c1 = 0
                elif tsum < 0:
                    c1 += 1
                else:
                    cm -= 1
            c2 -= 1
            cm = c2 - 1
            c1 = 0
        unique_list_of_tuples = list(set(tuple(sublist) for sublist in tl))
        unique_list_of_lists = [list(tupl) for tupl in unique_list_of_tuples]

        return unique_list_of_lists

