# Finger Exercise Lecture 5: Assume you are given a string variable named my_str. Write a piece of Python code that prints out a new string containing the even indexed characters of my_str. For example, if my_str = "abcdefg" then your code should print out aceg.

my_str = "abcdefg"
new = ''
# this loop prints add the even placed alphabets in the give string in the new string.
for i in range(0,len(my_str),2):
    new += my_str[i]
# This prints the even placed alphabets in  the "new" string.
print(new)
    