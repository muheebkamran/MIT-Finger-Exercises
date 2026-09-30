# page no 149:
# Finger exercise: The harmonic sum of an integer, n > 0, can be calculated using the formula \(1 + \frac{1}{2} + \dots + \frac{1}{n}\). Write a recursive function that computes this.
def recur_harmonic(n):
        """
    n: int > 0
    Returns the harmonic sum of n using recursion.
    Hint: Base case is when n = 1. Otherwise, in the recursive
    case you return (1/n) + recur_harmonic(n-1).
    """
        if n == 1:
            return 1
        else:
            return 1/n + recur_harmonic(n-1)

# Examples:
print(recur_harmonic(3))