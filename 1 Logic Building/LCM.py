# LCM of two numbers is the smallest number 
# which can be divided by both numbers. 

# brrute force 
def LCM(m, n):
    for i in range(1, m*n + 1):
        if i % m == 0 and i % n == 0:
            return i
    
m = 22
n = 18
print(LCM(m, n))



# An efficient solution is based on the below
# formula for LCM of two numbers ‘a’ and ‘b’.

# a x b = LCM(a, b) * GCD (a, b)
# LCM(a, b) = (a x b) / GCD(a, b)
# O(log(min(a,b))|O(log(min(a,b))

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a,b):
    return (a // gcd(a,b))* b

a = 15 
b = 20
print('LCM of', a, 'and', b, 'is', lcm(a, b))


