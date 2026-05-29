class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        c1 = 0
        c2 = len(numbers)-1
        while c1 < c2:
            tsum = numbers[c1] + numbers[c2]
            if tsum == target:
                return [c1+1,c2+1]
            elif tsum < target:
                c1 += 1
            elif tsum > target:
                c2 -= 1
        return [c1+1,c2+1]