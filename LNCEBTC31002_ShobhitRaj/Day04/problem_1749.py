def maxAbsoluteSum(nums):
    current_max = 0
    current_min = 0

    max_sum = 0
    min_sum = 0

    for num in nums:

        current_max = max(num, current_max + num)
        max_sum = max(max_sum, current_max)

        current_min = min(num, current_min + num)
        min_sum = min(min_sum, current_min)

    return max(max_sum, abs(min_sum))


nums = [1, -3, 2, 3, -4]

print(maxAbsoluteSum(nums))