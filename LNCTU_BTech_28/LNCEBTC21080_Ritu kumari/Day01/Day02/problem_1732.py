# Leetcode 1732 - Find the Highest Altitude
# Solution


class Solution:
    def largestAltitude(self,gain):
        altitude = 0
        highest = 0

        for value in gain:
            altitude += value
            highest = max(highest,altitude)

        return highest

# Example:
# Input: gain = [-5, 1, 5, 0, -7]
# output: 1