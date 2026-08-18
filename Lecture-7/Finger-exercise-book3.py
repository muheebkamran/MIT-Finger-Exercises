def is_in(s1,s2):
    """
    Write a function is_in that accepts two strings as
arguments and returns True if either string occurs anywhere in the
other, and False otherwise. Hint: you might want to use the built-in
str operator in
    """
    return s1 in s2 or s2 in s1

def test_is_in(s1_vals, s2_vals):
    for s1 in s1_vals:
        for s2 in s2_vals:
            result = is_in(s1, s2)
            if result:
                val = "in each other"
            else:
                val = "not in each other"
            print(f"s1 = '{s1}', s2 = '{s2}': {val}")


# Tuples of different string cases to test together
s1_vals = ("My name is Muheeb", "apple", "cat")
s2_vals = ("name", "orange", "at")

test_is_in(s1_vals, s2_vals)




