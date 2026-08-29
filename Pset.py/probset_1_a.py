# First Problem set: find the number of months it takes to save up for a down payment.
# The cost of your down payment is calculated by multiplying the total cost of your dream house by the down payment percentage.

# Ask the user for annual income, monthly savings rate, and house cost.
yearly_salary = float(input("Enter your annual income:"))
portion_saved = float(input("How much can you save per month %:"))  # Use decimal format, e.g. 0.10 for 10%
cost_of_dream_home = float(input('Whats the cost of your dream house:'))

# Calculate the total amount needed for the down payment (25% of house cost).
portion_down_payment = 0.25 * cost_of_dream_home

# Track the current savings and monthly income.
amount_saved = 0
monthly_income = yearly_salary / 12
r = 0.05  # Annual return rate on savings
saving = 0
months = 0

# Keep adding savings until the down payment goal is reached.
while amount_saved < portion_down_payment:
    months += 1
    saving = amount_saved * (r / 12)  # Interest earned this month
    amount_saved = amount_saved + monthly_income * portion_saved + amount_saved * (r / 12)

# Print the number of months needed to reach the down payment.
print('It will take you',months,'months')