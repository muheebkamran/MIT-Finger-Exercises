# practice lecture 12

def count_sqrts(nums_list):
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, including itself.
    """
    ps = 0
    for i in nums_list:
        if i ** 2 in nums_list:
            ps += 1
    return ps
# Examples:    
nums_list = [3,4,2,1,9,25]
print(count_sqrts(nums_list)) # prints 3