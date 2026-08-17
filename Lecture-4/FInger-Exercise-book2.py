# Finger exercise: Write a program that prints the sum of the prime
# numbers greater than 2 and less than 1000. Hint: you probably want
# to have a loop that is a primality test nested inside a loop that
# iterates over the odd integers between 3 and 999.

# Page no. 73
# A program to find th sum of all the prime no. in 1000:
sum_of_primes = 2
# Writing a a for loop that starts from 3 to 1000 and skips every even No. in its way to 1000
for prime in range (3,1000,2):
    prime_flag = True
    # writing another loop to divide every no. given by the prime loop and dividing it from 1 to 1000
    for divisor in range(2,prime):
        if prime % divisor == 0:
            prime_flag = False
            break
    if prime_flag:
            sum_of_primes += prime
print(sum_of_primes)






        