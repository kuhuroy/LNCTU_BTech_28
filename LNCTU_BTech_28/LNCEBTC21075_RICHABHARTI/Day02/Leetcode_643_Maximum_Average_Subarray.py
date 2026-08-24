# LeetCode 643 - Maximum Average Subarray

# Problem: Find maximum average of subarray with size k

def findMaxAverage(nums, k):
    # Step 1: Calculate sum of first k elements
    total = 0
    for i in range(k):
        total = total + nums[i]
    
    max_sum = total  # Store maximum sum
    
    # Step 2: Move window one element at a time
    for i in range(k, len(nums)):
        # Remove leftmost element from window
        total = total - nums[i - k]
        
        # Add new rightmost element to window
        total = total + nums[i]
        
        # Update maximum if current sum is greater
        if total > max_sum:
            max_sum = total
    
    # Step 3: Return average (divide by k)
    return max_sum / k


# Test
nums = [1, 12, -5, -6, 50, 3]
k = 4
result = findMaxAverage(nums, k)
print(f"Maximum average: {result}")
