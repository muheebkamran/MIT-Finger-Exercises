"""Finger exercise pg no. 129: Implement a function satisfying the following
specification. Hint: it will be convenient to use lambda in the body of
the implementation"""
def f(L1, L2):
    # Raise each value in L1 to its matching power in L2.
    powers = map(lambda x, y: x ** y, L1, L2)
    # Add all of the calculated powers together.
    return sum(powers)

# # or we can 

# def f(L1, L2):
# 	"""Return the sum of each element in L1 raised to the matching power in L2.

# 	For example, f([1, 2], [2, 3]) returns 9.
# 	"""
# 	summed = 0
# 	for i in range(len(L1)):
# 		summed += L1[i] ** L2[i] 
# 	return summed

print(f([1, 2], [2, 3]))
print(f([1, 2, 3], [0, 0, 0]))
print(f([0, 0], [2, 3]))        
print(f([-2, -3], [2, 3]))