nums = [1, 12, -5, -6, 50, 3]
k = 4

best_avg = None
for i in range(len(nums) - k + 1):
    total = 0
    for j in range(i, i + k):
        total += nums[j]
    average = total / k
    if best_avg is None or average > best_avg:
        best_avg = average

print("Maximum average of a subarray of length", k, "is", best_avg)
