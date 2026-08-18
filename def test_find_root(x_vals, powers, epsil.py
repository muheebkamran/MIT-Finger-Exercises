def find_root(x, power, epsilon):
    """Finds the root of x using bisection search."""
    # Negative numbers do not have even real roots
    if x < 0 and power % 2 == 0:
        return None
        
    # Set search boundaries
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low) / 2.0
    
    # Bisection search loop
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans

def test_find_root(x_vals, powers, epsilons):
    for x in x_vals:
        for p in powers:
            for e in epsilons:
                result = find_root(x, p, e)
                
                if result is None:
                    val = 'No root exists'
                else:
                    # Nested inside else to prevent NoneType crash
                    if abs(result**p - x) > e:
                        val = 'Bad'
                    else:
                        val = 'Okay'
                        
                print(f'x = {x}, power = {p}, epsilon = {e}: {val}')

x_vals = (0.25, 8, -8)
powers = (1, 2, 3)
epsilons = (0.1, 0.001, 1)

test_find_root(x_vals, powers, epsilons)