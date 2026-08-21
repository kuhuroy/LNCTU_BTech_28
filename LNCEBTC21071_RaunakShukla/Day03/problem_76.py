class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        need = Counter(t)
        left = 0
        ans = ""

        for right in range(len(s)):
            need [s[right]] -=1

            while all(v <=0 for v in need.values()):
                if not ans or right - left + 1 < len(ans):
                    ans = s[left:right +1]

                need[s[left]] += 1
                left += 1
        return ans    
        