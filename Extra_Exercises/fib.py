fibonacci_numbers = [0, 1]
while len(fibonacci_numbers) < 10:
    # Calculate the next number by adding the last two numbers
    next_num = fibonacci_numbers[-1] + fibonacci_numbers[-2]
    fibonacci_numbers.append(next_num)

file_name = "fib_file.txt"
# FIX 1: Use your file_name variable instead of "fib_file"
with open(file_name, 'w') as file:
    for i in fibonacci_numbers: 
        # FIX 2: file.write() only takes one string argument. Convert 'i' to a string.
        file.write(str(i) + '\n')

# FIX 3: Match the file name variable here too so it doesn't crash
with open(file_name, 'r') as text:
    for i in text:
        # FIX 4: Use strip() so it doesn't print extra double blank lines
        print(i.strip())
