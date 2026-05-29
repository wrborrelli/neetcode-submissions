class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            None
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict.keys():
                s_dict[s[i]] = 1
            elif s[i] in s_dict.keys():
                s_dict[s[i]] += 1
            if t[i] not in t_dict.keys():
                t_dict[t[i]] = 1
            elif t[i] in t_dict.keys():
                t_dict[t[i]] += 1
        if s_dict.keys() != t_dict.keys():
            return False
        else:
            None
        for key in s_dict.keys():
            test = s_dict[key] == t_dict[key]
            if test:
                None
            else:
                return False
        return True
        
