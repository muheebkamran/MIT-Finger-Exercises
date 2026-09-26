# pg no 139 
def get_min(d):

     """d a dict mapping letters to ints
    returns the value in d with the key that occurs first
    in the
    alphabet. E.g., if d = {x = 11, b = 12}, get_min
    returns 12."""
     for k,v in d.items():
         if k == min(d):
             return v
d = {
    'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15, 'f': 16, 'g': 17, 
    'h': 18, 'i': 19, 'j': 20, 'k': 21, 'l': 22, 'm': 23, 'n': 24, 
    'o': 25, 'p': 26, 'q': 27, 'r': 28, 's': 29, 't': 30, 'u': 31, 
    'v': 32, 'w': 33, 'x': 34, 'y': 35, 'z': 36
}
print(get_min(d))