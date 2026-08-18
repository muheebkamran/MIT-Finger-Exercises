# Finger exercise on page 93 using figure 4-3 to add the values of three approx sq

def find_root(x, power, epsilon):
    # Find interval containing answer
    if x < 0 and power%2 == 0:
        return None #Negative number has no even-powered roots
    low = min(-1, x)
    high = max(1, x)
    # Use bisection search
    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans
root1 = find_root(25, 2, 0.001)
root2 = find_root(-8, 3, 0.001)
root3 = find_root(16, 4, 0.001)

total = root1 + root2 + root3
# wrote these print statement just so i know what the values of all of the root were not to get confuses by seeing 5 or 4.9 as an ans
# print(root1)
# print(root2)
# print(root3)
print(total)
