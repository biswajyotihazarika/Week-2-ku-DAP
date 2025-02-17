def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return set(s.lower()) >= alphabet

# Example usage
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # Output: True
print(is_pangram("Hello world"))  # Output: False