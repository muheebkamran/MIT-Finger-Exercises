x = 8
y = 9
z = 23

answer = min(x, y, z)
# greatest odd number
if x%2 != 0:
    answer = x
if y%2 != 0 and y > answer:
    answer = y
if z%2 != 0 and z > answer:
    answer = z
print(answer)