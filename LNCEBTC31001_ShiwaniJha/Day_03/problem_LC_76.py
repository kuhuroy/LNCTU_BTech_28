class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if n > m:  # t cannot fit inside s
            return ""
        freq = {}  # Required char frequencies
        for i in t:   # Count chars in t
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        count = {}   # Char frequencies in curr window
        l = 0  # left ptr
        r = 0  # right ptr
        valid = 0   # No. of satisfied char requirements
        req = len(freq)   # Number of unique characters required
        ans = ""  # Store minimum window
        mini = float('inf') # Store mini window len
        while r < m:   # Expand window using r
            ch = s[r]   # Curr char
            if ch in count:
                count[ch] += 1 
            else:
                count[ch] = 1
            if ch in freq and count[ch] == freq[ch]:  # Req freq for this char is satisfied
                valid += 1
            while valid == req:  # Window contains all req char
                if r-l+1 < mini:   # Update minimum window
                    mini = r-l+1
                    ans = s[l : r+1]
                left = s[l]   # Char being removed
                count[left] -= 1
                if left in freq and count[left] < freq[left]:  # Removing it makes the window invalid
                    valid -= 1
                l += 1   # Shrink window
            r  += 1 # Expand window
        return ans


#  Time: O(m + n)
# Space: O(m + n) 

'''
76. Minimum Window Substring
Solved
Hard
Topics
premium lock icon
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?



'''
