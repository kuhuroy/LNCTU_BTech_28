# LeetCode 1732 - Highest Altitude

# Problem: Find highest altitude during journey

def largestAltitude(gain):
    altitude = 0  # Current altitude
    max_altitude = 0  # Track highest
    
    for g in gain:
        altitude += g
        max_altitude = max(max_altitude, altitude)
    
    return max_altitude


# Test
gain = [-5, 1, 5, 0, -7]
result = largestAltitude(gain)
print(f"Highest altitude: {result}")  # 5
