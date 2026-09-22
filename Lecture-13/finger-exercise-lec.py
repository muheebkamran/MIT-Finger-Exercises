def sum_str_lengths(L):
    """L is a non-empty list containing either:
    * string elements or
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and lengths of strings in the sublists of L.
    If L contains an element that is not a string or a list, or L's sublists contain an element that is not a string, raise a ValueError.
    """
    total = 0
    for i in L:
        if type(i) == str:
            total += len(i)
        elif type(i) == list:
            for e in i:
                if type(e) == str:
                    total += len(e)
                else:
                    raise ValueError("Sublist contains a type int element")
        else:
            raise ValueError("List contains an element that is not a string or a list is int")
    return total


# Examples:
# print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
# print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError