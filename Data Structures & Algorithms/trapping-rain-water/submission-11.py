class Solution:
    def trap(self, height: List[int]) -> int:
        total_area = 0
        if len(height) == 1:
            return 0
        elif len(height) == 3:
            temp_area = 0
            for i in height:
                if i < min([height[0], height[-1]]):
                    temp_area += min([height[0], height[-1]]) - i
                else:
                    temp_area += 0
            total_area += temp_area
            return total_area
        starter = 0
        current = []
        while height[starter] == 0:
            starter += 1
        while starter < len(height)-1:
            print("starter: ",starter,' height: ',height[starter])
            current.append(height[starter])
            print('diff',height[starter+1] - height[starter])
            if height[starter+1] - height[starter] > 0 and height[starter+1] >= max(current):
                print('basin detected')
                current.append(height[starter+1])
                print('current basin: ',current)
                temp_area = 0
                print('basis end points: ',current[0], current[-1])
                print('basin height',min([current[0], current[-1]]))
                for i in current:
                    if i < min([current[0], current[-1]]):
                        temp_area += min([current[0], current[-1]]) - i
                    else:
                        temp_area += 0
                print('basin area:',temp_area)
                total_area += temp_area
                current = []
                starter += 1
            elif height[starter+1] - height[starter] < 0:
                print('maybe a basin start')
                starter += 1
            else:
                print('not a basin start')
                starter += 1
        if height[-1] > height[-2]:
            current.append(height[-1])
        temp_area = 0
        for i in current:
            if i < min([current[0], current[-1]]):
                temp_area += min([current[0], current[-1]]) - i
            else:
                temp_area += 0
        total_area += temp_area
        return total_area
