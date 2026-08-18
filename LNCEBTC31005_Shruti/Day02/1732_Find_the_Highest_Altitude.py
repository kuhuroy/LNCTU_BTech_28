class Solution:

    def largestAltitude(self, gain):

        # We start from altitude 0
        current_altitude = 0

        # At the beginning, the highest altitude is also 0
        highest_altitude = 0

        # Go through every value in the gain list
        for change in gain:

            # Add the current change to our altitude
            current_altitude = current_altitude + change

            # Check if the current altitude is higher
            # than the highest altitude we have found
            if current_altitude > highest_altitude:

                # If it is higher, update highest altitude
                highest_altitude = current_altitude

        # Return the highest altitude
        return highest_altitude
