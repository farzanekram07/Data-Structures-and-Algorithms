# Given two numbers a and b, the task is 
# to find the GCD of the two numbers.

# my writing
# brute force - O(min(m,n))|O(min(m,n))
# very slow - think 10^6 (million operations)
def GCD(m, n):
    new_arr = []
    value = min(m,n)
    for i in range(1, value+1):
        if m % i == 0 and n % i == 0:
            new_arr.append(i)
    return new_arr[-1]

m = 36
n = 60
print(GCD(m, n))



# still brute force but smarter
def GCD1(m, n):
    value = min(m, n)
    for i in range(value, 0, -1):
        if m % i == 0 and n % i == 0:
            return i
        
m = 36
n = 60
print(GCD1(m,n))



# optimal - O(log(min(a,b)))
# iterative - Eucledian way
def GCD2(m, n):
    while n:
        m, n = n, m % n
    return m

m = 60
n = 36
print(GCD2(m, n))


# recursive - O(log(min(a,b)))
def GCD3(m, n):
    if n == 0:
        return m
    return GCD3(n, m % n)

m = 36
n = 60
print(GCD3(m, n))


# note -  Edge case:
# For very large numbers, Python's 
# recursion depth can be hit. 
# In such cases, iterative is safer.



# Using Built-in Functions - O(log(min(a,b)))
import math

a = 98
b = 56
gcd_result = math.gcd(a, b)
print(f"The gcd of {a} and {b} is", gcd_result)