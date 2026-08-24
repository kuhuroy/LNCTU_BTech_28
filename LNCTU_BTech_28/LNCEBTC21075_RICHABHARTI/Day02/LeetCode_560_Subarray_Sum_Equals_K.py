# LeetCode 560 - Subarray Sum Equals K

# Problem: Count subarrays with sum equal to k

def subarraySum(nums, k):
    count = 0
    
    # Check all subarrays
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total == k:
                count += 1
    
    return count


# Test
nums = [1, 1, 1]
k = 2
result = subarraySum(nums, k)
print(f"Result: {result}")  # 2
