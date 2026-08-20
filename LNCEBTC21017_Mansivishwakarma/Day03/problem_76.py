class Solution:
    def minWindow(self, s, t):
        from collections import Counter
        d = Counter(t)
        l = c = 0
        ans = ""

        for r, x in enumerate(s):
            d[x] -= 1
            if d[x] >= 0: c += 1
            while c == len(t):
                if not ans or r-l+1 < len(ans): ans = s[l:r+1]
                d[s[l]] += 1
                if d[s[l]] > 0: c -= 1
                l += 1
        return ans
