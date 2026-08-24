def sum_range(nums, left, right):
    if left < 0 or right >= len(nums) or left > right:
        raise ValueError("Invalid range")
    return sum(nums[left:right + 1])


if __name__ == "__main__":
    nums_input = input("Enter numbers separated by spaces: ")
    nums = [int(x) for x in nums_input.split()]

    left = int(input("Enter left index: "))
    right = int(input("Enter right index: "))

    result = sum_range(nums, left, right)
    print(f"Sum of nums[{left}:{right}] = {result}")
