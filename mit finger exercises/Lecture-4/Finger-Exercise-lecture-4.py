N = int(input("Enter a perfect cube number: "))
# Find the cube root of N
guess = 0
while guess**3 < N:
    guess += 1
if guess**3 == N:
    print(f"{N} is a perfect cube of {guess}.")
else:
    print("error")