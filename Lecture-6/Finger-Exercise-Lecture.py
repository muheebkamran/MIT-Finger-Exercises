# Finger Exercise Lecture 6: Assume you are given an integer 0 <= X <= 1000. Write a piece of Python code that uses bisection search to guess N. The code prints two lines: count: with how many guesses it took to find N, and answer: with the value of N. Hints: If the halfway value is exactly in between two integers, choose the smaller one
x = int(input('Enter any value between 1 to 1000: '))
low = 0
high = 1000
guess = (low + high) // 2
num_guesses = 1
# this while loop run till the time guess is not equal to x
while guess != x:
    if guess < x:
        low = guess
    else:
        high = guess
    guess = (low + high) // 2
    num_guesses += 1

print('Num of guesses:',num_guesses)
print('Guess:',guess)