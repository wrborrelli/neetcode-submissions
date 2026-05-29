from collections import defaultdict

def check_in(s1,s2):
    dd_s1 = defaultdict(int)
    dd_s2 = defaultdict(int)
    for i in s1:
        dd_s1[i]+=1
    for i in s2:
        dd_s2[i]+=1
    
    out = 0
    s1_uni = list(set(list(s1)))
    for i in s1_uni:
        if dd_s1[i] <= dd_s2[i]:
            pass
        else:
            out+=1
    for i in s1:
        if i in s2:
            pass
        else:
            out+=1
    
    if out != 0:
        return False
    else:
        return True

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        shortest = ""
        p1=0
        p2=1
        while p2<=len(s)+1:
            mcheck = check_in(t,s[p1:p2])
            if mcheck:
                if shortest == "" or len(s[p1:p2]) < len(shortest):
                    shortest = s[p1:p2]
                p1+=1
            else:
                p2+=1
        return shortest