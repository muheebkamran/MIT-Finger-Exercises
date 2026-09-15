"""
Problem Set 1b: Down Payment Calculator
Determines the number of months required to save enough money for a house down payment
while accounting for interest earnings and semi-annual salary raises.
"""

# Get user input
yearly_salary = float(input("Enter your annual income:"))
portion_saved = float(input("How much can you save per month %:"))  # Enter as decimal (e.g., 0.10 for 10%)
cost_of_dream_home = float(input('Whats the cost of your dream house:'))
semi_annual_raise = float(input('Enter the raise:'))

# Initialize financial parameters
portion_down_payment = 0.25 * cost_of_dream_home  # 25% down payment required
amount_saved = 0  # Running total of savings with interest
monthly_income = yearly_salary / 12  # Convert annual salary to monthly
annual_return_rate = 0.05  # 5% annual return on savings
months = 0  # Month counter

# Simulate month-by-month savings with compound interest and raises
while amount_saved < portion_down_payment:
    months += 1
    # Apply semi-annual raise every 6 months
    if months % 6 == 0:
        monthly_income += monthly_income * semi_annual_raise
    # Update savings: add monthly contribution and compound interest
    amount_saved = amount_saved + monthly_income * portion_saved + amount_saved * (annual_return_rate / 12)

# Display result
print('It will take you', months, 'months')