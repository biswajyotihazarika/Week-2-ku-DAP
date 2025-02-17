def is_perfect(number):
    if number < 1:
        return False
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

# Example usage:
num = 28  # 28 is a perfect number (1 + 2 + 4 + 7 + 14 = 28)
print(is_perfect(num))  # Output: True
