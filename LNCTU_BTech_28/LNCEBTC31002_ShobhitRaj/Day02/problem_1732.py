class Solution:
    def largestAltitude(self, gain):
        altitude = 0
        highest = 0

        for i in gain:
            altitude += i
            highest = max(highest, altitude)

        return highest