sum = 2

for i in range(3, 1000, 2):
    prime = True
    check = int(i**0.5)
    for j in range(2, check + 1):
        if i % j == 0:
            prime = False
            break
    if prime:
        sum += i
print(sum)