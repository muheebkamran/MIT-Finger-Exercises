number = int(input("Enter a number: "))
# Determine if the number is even, odd, or zero
if number % 2 == 0:
    print("The number is even.")
elif number % 2 != 0:
    print("The number is odd.")
else:
    print("Zero is neither even nor odd.")