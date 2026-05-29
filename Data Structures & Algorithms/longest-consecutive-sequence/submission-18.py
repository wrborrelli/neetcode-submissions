class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        countf = 1
        countb = 1
        if len(nums) == 0:
            return 0
        
        counts = []
        counter = 1
        i=0
        print(nums)
        while i < len(nums)-1:
            print(nums[i],nums[i+1])
            diff = abs(nums[i+1] - nums[i])
            if diff == 1:
                print('diff is 1')
                counter += 1
            else:
                print('diff isnt 1')
                counts.append(counter)
                counter = 1
            i += 1
        print(counts)
        if i == len(nums)-1:
            counts.append(counter)
        return max(counts)