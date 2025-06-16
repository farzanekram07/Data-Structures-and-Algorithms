# iterative approach - from n-m to n+m
def closest(n, m):
    closest = 0
    min_difference = float('inf')

    for i in range(n - abs(m), n + abs(m) + 1):
        if i % m == 0:
            difference = abs(n-i)

            if difference < min_difference or \
            (difference == min_difference and \
             abs(i) > abs(closest)):
                closest = i
                min_difference = difference
    return closest

n = -15
m = 6
print(closest(n, m)) 


# by finding quotient
def closest_number(n, m):
    q = int(n/m)
    n1 = q * m

    if ((n*m) > 0):
        n2 = (m * (q+1))
    else:
        n2 = (m * (q-1))

    if (abs(n-n1) < abs(n-n2)):
        return n1
    else:
        return n2
    
n = 13; m = 4
print(closest_number(n,m))
