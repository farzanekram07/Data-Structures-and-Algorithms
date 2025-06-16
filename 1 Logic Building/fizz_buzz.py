# Given an integer n, for every positive integer 
# i <= n, the task is to print,

# “FizzBuzz” if i is divisible by 3 and 5,
# “Fizz” if i is divisible by 3,
# “Buzz” if i is divisible by 5
# “i” as a string, if none of the conditions are true.
# Examples:

# Input: n = 3
# Output: [“1”, “2”, “Fizz”]


# brute force - O(n)|O(n)
# by checking every integer
def fizz_buzz(n):
    list = []
    for i in range(1, n+1):        
        if i % 3 == 0 and i % 5 == 0:
            list.append("FizzBuzz")
        elif i % 3 == 0:
            list.append("Fizz")
        elif i % 5 == 0:
            list.append("Buzz")
        else:
            list.append(str(i))
    return list

n = int(input())
print(fizz_buzz(n))


# better approach
def fizz_buzz1(n):
    res = []
    
    for i in range(1, n+1):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        if not s:
            s += str(i)
        res.append(s)
    return res

n = int(input())
res = fizz_buzz1(n)
for i in res:
    print(i, end = " ")
print()


# hashing
def fizzBuzz(n):
    res = []  

    mp = {3: "Fizz", 5: "Buzz"}
    divisors = [3, 5] 

    for i in range(1, n + 1):
        s = ""  

        for d in divisors: 
            if i % d == 0:
                s += mp[d]
        if not s:
            s += str(i)
        res.append(s)
    return res

n = 20
res = fizzBuzz(n)

for s in res:
    print(s, end=" ") 
print()