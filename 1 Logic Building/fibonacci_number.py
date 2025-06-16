# Given a positive integer n, the task is to 
# find the nth Fibonacci number.

# The Fibonacci sequence is a sequence where 
# the next term is the sum of the previous 
# two terms. The first two terms of the 
# Fibonacci sequence are 0 followed by 1. 
# The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21


## Recursion
#  plain recursion - O(2^n)|O(n)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = 10
result = fib(n)
print(f"The fibonacci of {n} is {result}")


# Recursion + Memoization
# dictionary based memoization in fibonacci
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    memo[n] = fibonacci(n-1, memo) + \
    fibonacci(n-2, memo)
    return memo[n]

n = 10
print(fibonacci(n))


# list based memoization in fibonacci
def fib(n, memo):
    if memo[n] != -1:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

n = 10
memo = [-1] * (n+1)
print(fib(n, memo))







## Iteration
#  DP tabulation - bottom up approach
def tabulative_fib(n):
    if n <= 1:
        return n
    
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = 10
print(tabulative_fib(n))


# space optimized - O(n)|O(1)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for i in range(2, n+1):
        fib = a + b
        a = b
        b = fib
    return fib       
        
n = 10
print(fibonacci(n))



## Matrix exponentiation is pending


# Golden ratio - Binet's Formula
# correct value if n < 70
import math

def fib2(n):
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2

    fib_n = (phi ** n) / sqrt5
    return round(fib_n)

n = 10
print(fib2(n))