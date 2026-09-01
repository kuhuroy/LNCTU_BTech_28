def longestOnes(nums, k):
    left = 0
    zeros = 0
    ans = 0

    for right in range(len(nums)):

        if nums[right] == 0:
            zeros += 1

        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

print(longestOnes(nums, k))