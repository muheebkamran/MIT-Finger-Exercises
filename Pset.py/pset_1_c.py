# Get initial deposit from user
initial_deposit = float(input('Enter Initial deposit:'))
cost_of_the_house = 800_000
down_payment = 0.25 * 800_000  # Target amount needed
amount_saved = 0
num_of_guesses = 0

# Binary search bounds for interest rate
high = 1
low = 0
r = (high + low) / 2  # Current guess for annual interest rate

# Binary search: find interest rate that reaches target in 3 years (36 months)
while not(199900 < amount_saved < 200100):
    amount_saved = initial_deposit * ((1+(r/12))**36)  # Compound interest formula
    num_of_guesses += 1
    if amount_saved < 199900:  # Too low, increase rate
        low = r
    else:  # Too high, decrease rate
        high = r
    r = (high + low)/2  # Adjust guess
    
# Output the found interest rate and number of iterations
print(r,num_of_guesses)