class Solution:
    def isPalindrome(self, s: str) -> bool:
        taken = []
        for c in s:
            if c.isalnum():
                taken.append(c.lower())
            else:
                None
        bl = taken.copy()
        bl.reverse()
        fs = ''.join(taken)
        bs = ''.join(bl)
        print(fs,bs)
        return fs == bs