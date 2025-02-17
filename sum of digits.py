def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

# Example usage
print(sum_of_digits(12345))  # Output: 15 (1 + 2 + 3 + 4 + 5)
