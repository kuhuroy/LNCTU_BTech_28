from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = Counter(t)
        have = {}
        left = 0
        formed = 0
        required = len(need)

        ans = float("inf"), None, None

        for right in range(len(s)):
            char = s[right]
            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                left_char = s[left]
                have[left_char] -= 1

                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]