# IDK man it was just easy 
def is_in(s1,s2):
    """
    Write a function is_in that accepts two strings as
arguments and returns True if either string occurs anywhere in the
other, and False otherwise. Hint: you might want to use the built-in
str operator in
    """
    # if s1 in s2 or s2 in s1:
    #     return True
    # else:
    #     return False
    # we could use if but cleaner version of it im=n function is just saying return it cause it is already a bolean
    return s1 in s2 or s2 in s1
s1 =" My name is Muheeb"
s2 = "name"
print(is_in(s1,s2))