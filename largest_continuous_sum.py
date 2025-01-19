def largest_continuous_sum(nums):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    current_sum = 0  # Initialize current_sum to 0

    for num in nums:
        current_sum += num  # Add the current number to current_sum
        max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is larger

        if current_sum < 0:
            current_sum = 0  # Reset current_sum to 0 if it becomes negative

    return max_sum

# Test the function
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(largest_continuous_sum(nums))
