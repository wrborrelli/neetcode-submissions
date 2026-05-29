def check(l1,l2):
    if l1==l2:
        return True
    else:
        return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #if len(s1) > len(s2):
        #    return False
        if len(set(list(s1))) > len(set(list(s2))):
            return False
        tl1=sorted(list(s1))
        tl2=list(s2)
        for p in range(len(s2)):
            #print(tl1,sorted(tl2[p:p+len(tl1)]))
            if check(tl1,sorted(tl2[p:p+len(tl1)])):
                return True
            else:
                pass
        return False