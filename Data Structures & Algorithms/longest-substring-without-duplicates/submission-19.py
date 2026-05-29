class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s.strip() == '':
            s = s.replace(' ','s')
        if s == '':
            return 0
        tl = list(s)
        p1=0
        p2=1
        lengths = []
        while p2<=len(tl):
            if len(tl[p1:p2]) == len(set(tl[p1:p2])):
                lengths.append(len(tl[p1:p2]))
                p2+=1
            else:
                p1+=1
                p2+=1
        return max(lengths)