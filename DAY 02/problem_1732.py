class Solution:
    def largestAltitude(self, gain):
        altitude = 0
        highest = 0

        for g in gain:
            altitude += g
            highest = max(highest, altitude)

        return highest


gain = [-5, 1, 5, 0, -7]

obj = Solution()
print(obj.largestAltitude(gain))