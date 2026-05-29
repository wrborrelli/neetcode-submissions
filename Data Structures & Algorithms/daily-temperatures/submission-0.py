class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = []
        c0 = 0
        while c0 < len(temperatures) - 1:
            print('t0: ',temperatures[c0])
            smaller = True
            c1 = c0 + 1
            count = 0
            while smaller:
                if c1 == len(temperatures):
                    print('no t2 bigger')
                    days.append(0)
                    break
                if temperatures[c1] > temperatures[c0]:
                    count += 1
                    days.append(count)
                    smaller = False
                    print('bigger t2 is ',temperatures[c1],' ',count,' days away')
                else:
                    c1 += 1
                    count += 1
            c0 += 1
        days.append(0)
        return days
