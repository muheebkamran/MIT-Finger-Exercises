# Finger exercise page no. 79
x = float(input("Enter a value: "))
epsilon = 0.01
num_guesses = 0

# Check if input is negative and work with its absolute value
is_negative = x < 0
val = abs(x)

if val >= 1:
    low = 1.0
    high = val
else:
    low = val
    high = 1.0

guess = (high + low) / 2.0
# Loop runs till the time it doesnt find the cube of the number given
while abs(guess**3 - val) >= epsilon:
    # print(f'low = {low} and high = {high} and guess is {guess}')
    if guess**3 < val:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    num_guesses += 1

print("No. of Guesses are = ", num_guesses)

if is_negative:
    print(f"Your guess is {guess}i (or {guess}j)")
else:
    print("Your guess is", guess)