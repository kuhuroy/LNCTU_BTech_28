def minWindow(s, t):
    if len(t) > len(s):
        return ""

    count = {}

    for ch in t:
        count[ch] = count.get(ch, 0) + 1

    left = 0
    required = len(t)
    min_length = float("inf")
    start = 0

    for right in range(len(s)):
        if s[right] in count:
            if count[s[right]] > 0:
                required -= 1

            count[s[right]] -= 1

        while required == 0:

            if right - left + 1 < min_length:
                min_length = right - left + 1
                start = left

            if s[left] in count:
                count[s[left]] += 1

                if count[s[left]] > 0:
                    required += 1

            left += 1

    if min_length == float("inf"):
        return ""

    return s[start:start + min_length]


s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s, t))