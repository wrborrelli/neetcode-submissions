from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        p1 = 0
        maxf = 0
        longest = 0

        for p2 in range(len(s)):
            count[s[p2]] += 1
            maxf = max(maxf, count[s[p2]])

            while (p2 - p1 + 1) - maxf > k:
                count[s[p1]] -= 1
                p1 += 1

            longest = max(longest, p2 - p1 + 1)

        return longest