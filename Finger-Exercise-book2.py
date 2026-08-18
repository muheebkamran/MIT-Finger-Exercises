def is_in(s1,s2):
    """
    Write a function is_in that accepts two strings as
arguments and returns True if either string occurs anywhere in the
other, and False otherwise. Hint: you might want to use the built-in
str operator in
    """
    if s1 in s2 or s2 in s1:
        return True
    else:
        return False
s1 =" My name is Muheeb"
s2 = "name"
print(is_in(s1,s2))