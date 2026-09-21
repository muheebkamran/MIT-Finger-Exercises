# page no. 192: 'Finger exercise: Implement a function that meets the specification below. Use a try-except block. Hint: before starting to code, you might want to type something like 1 + 'a' into the shell to see whatkind of exception is raised.'
def sum_digits(s):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""
    summed = 0
    try:
        for i in s:
            if i in '1234567890':
                summed += int(i)
        return summed
    except TypeError,ValueError:
        return("Entered a wrong value")
print(sum_digits(123))
print(sum_digits('a2b3c'))