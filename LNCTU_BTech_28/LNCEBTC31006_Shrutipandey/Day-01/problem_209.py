class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        # Left pointer of the sliding window
        left = 0

        # Current sum of the window
        current_sum = 0

        # Store minimum length
        # len(nums) + 1 means no valid subarray found yet
        min_length = len(nums) + 1

        # Right pointer moves through the array
        for right in range(len(nums)):

            # Add current number to the window
            current_sum += nums[right]

            # If sum becomes >= target,
            # try to make the window smaller
            while current_sum >= target:

                # Calculate current window length
                current_length = right - left + 1

                # Update minimum length
                min_length = min(min_length, current_length)

                # Remove leftmost element
                current_sum -= nums[left]

                # Move left pointer forward
                left += 1

        # If min_length was never updated,
        # no valid subarray exists
        if min_length == len(nums) + 1:
            return 0

        return min_length