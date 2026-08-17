# Page no. 72
# Finger exercise: Write a program that asks the user to enter an
# integer and prints two integers, root and pwr, such that 1 < pwr < 6
# and root**pwr is equal to the integer entered by the user. If no such
# pair of integers exists, it should print a message to that effect
n = int(input("Enter number: ")) 
flag = False 
# first loop goes from 2 to 5
for pwr in range(2, 6): 
    guess = 0 
    while guess**pwr < n: 
        guess += 1 
    if guess**pwr == n: 
        print(f"{guess}**{pwr} = {n}") 
        flag = True 
if not flag: 
    print("error")