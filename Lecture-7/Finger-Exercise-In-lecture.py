def is_even(i):
    """
    Input:i, a positive int
    Return True if i is even, False otherwise
    """
    return i % 2 == 0

print(is_even(6))
print(is_even(4))

def div_by(n, d):
    """
    n and d are ints > 0
    Return True if d divides n evenly, False otherwise
    """
    return n % d == 0

print(div_by(10, 3))
print(div_by(195, 13))
