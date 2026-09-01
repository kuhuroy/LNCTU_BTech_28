def maxSubarraySumCircular(nums):
    total = sum(nums)

    # Normal maximum subarray sum
    current_max = 0
    max_sum = nums[0]

    for num in nums:
        current_max = max(num, current_max + num)
        max_sum = max(max_sum, current_max)

    # Minimum subarray sum
    current_min = 0
    min_sum = nums[0]

    for num in nums:
        current_min = min(num, current_min + num)
        min_sum = min(min_sum, current_min)

    # If all numbers are negative
    if max_sum < 0:
        return max_sum

    # Circular maximum sum
    circular_sum = total - min_sum

    return max(max_sum, circular_sum)


nums = [5, -3, 5]

print(maxSubarraySumCircular(nums))