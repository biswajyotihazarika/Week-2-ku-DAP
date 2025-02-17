def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage:
nums = [2, 3, 4, 5]
print(multiply_list(nums))  # Output: 120
