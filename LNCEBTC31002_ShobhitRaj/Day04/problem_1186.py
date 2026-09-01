def maximumSum(arr):
    # max_sum = maximum sum without deletion
    # delete_sum = maximum sum with one deletion

    max_sum = arr[0]
    delete_sum = 0
    answer = arr[0]

    for i in range(1, len(arr)):
        delete_sum = max(max_sum, delete_sum + arr[i])
        max_sum = max(arr[i], max_sum + arr[i])

        answer = max(answer, max_sum, delete_sum)

    return answer


arr = [1, -2, 0, 3]

print(maximumSum(arr))