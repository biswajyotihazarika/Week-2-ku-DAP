def generate_random_numbers():
    return [random.randint(1, 100) for _ in range(4)]

# Example usage
print(generate_random_numbers())