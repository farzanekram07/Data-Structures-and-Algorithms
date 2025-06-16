# Given two integer arrays a[] and b[] containing
# two integers each representing the numerator 
# and denominator of a fraction respectively. 
# The task is to find the sum of the two fractions 
# and return the numerator and denominator of the result.

# Example 
# Input:  a = [1, 2] , b = [3, 2] 
# Output: [2, 1] 
# Explanation: 1/2 + 3/2 = 2/1


# brute force - O(log(min(a, b))|O(1)
from math import gcd

def add_fraction(a, b):
    denom = (a[1] * b[1]) // gcd(a[1], b[1])
    num = (a[0] * (denom // a[1])) + (b[0] * (denom // b[1]))

    common_factor = gcd(num, denom)
    denom //= common_factor
    num //= common_factor

    return[num, denom]

a = [1, 2]
b = [3, 2]
ans = add_fraction(a, b)
print(f"{ans[0]}, {ans[1]}")



# find a addition of a fraction of a list
from math import gcd

def add_fraction_list(fractions):
    num, denom = fractions[0]

    for i in range(1, len(fractions)):
        next_num, next_denom = fractions[i]

        lcm = (denom * next_denom) // gcd(denom, next_denom)
        num = num * (lcm // denom) + next_num * (lcm // next_denom)

        denom = lcm
        common_factor = gcd(num, denom)

        num //= common_factor
        denom //= common_factor

    return f"{num}, {denom}"

fractions = [[1, 2], [1, 3], [1, 6]]
results = add_fraction_list(fractions)
print(results)


# using recursion
def add_two_fraction(a, b):
    denom = (a[1] * b[1]) // gcd(a[1], b[1])
    num = (a[0] * (denom // a[1])) + (b[0] * (denom // b[1]))

    common_factor = gcd(num, denom)
    denom //= common_factor
    num //= common_factor

    return[num, denom]

def add_fraction_recursive(fractions):
    if len(fractions) == 1:
        return fractions[0]
    return add_two_fraction(fractions[0], add_fraction_recursive(fractions[1:]))

fractions = [[1, 2], [1, 3], [1, 6]]
num, den = add_fraction_recursive(fractions)
print(f"{num}/{den}") 