# A number is a perfect number if is equal to
# the sum of its proper divisors, that is, 
# the sum of its positive divisors excluding 
# the number itself. The task is to find 
# whether a given positive integer n is 
# perfect or not.

# Example:
# Input: n = 15
# Output: false
# Divisors of 15 are 1, 3 and 5. Sum of 
# divisors is 9 which is not equal to 15.

# Input: n = 6
# Output: true
# Divisors of 6 are 1, 2 and 3. Sum of 
# divisors is 6.


# brute force
def perfect_number(n):
    new_arr = []
    for i in range(1, n):
        if n % i == 0:
            new_arr.append(i)

    total = sum(new_arr)
    if total == n:
        return True
    else:
        return False

n = int(input())
print(perfect_number(n))


# improvision
def perfect_number1(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

n = int(input())
print(perfect_number1(n))

