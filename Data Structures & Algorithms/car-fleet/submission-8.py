class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(range(len(speed)), reverse=True, key=lambda i: position[i])
        print(cars)
        ans = len(speed) + 1
        curr = cars[0]
        for c in cars:
            print((target - position[c]) / speed[c],(target - position[curr]) / speed[curr])
            if (target - position[c]) / speed[c] <= (target - position[curr]) / speed[curr]:
                ans -= 1
            else:
                curr = c
        return ans
