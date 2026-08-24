#LeetCode 209- Minimum Size Subarray Sum

# Simple, logic-focused sliding-window solution
def min_subarray_len(target, nums):
    left = total = 0
    min_len = len(nums) + 1   # infinity 
    for right, v in enumerate(nums):
        total += v
        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]; left += 1
    return 0 if min_len > len(nums) else min_len


if __name__ == '__main__':
	# simple example
	print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))  # Output 2


