# Write an efficient program to count the 
# number of 1s in the binary representation 
# of an integer.

# Examples : 
# Input : n = 6
# Output : 2
# Binary representation of 6 is 110 
# and has 2 set bits


# brute force - O(logn)|O(1)
def count_bits(n):
    count = 0
    for _ in range(n):
        count += n & 1
        n >>= 1
    return count

n = 15
print(count_bits(n))

 
# recursion 
def count_set_bits(n):
    
    if n == 0:
        return 0
    else:
        return (n & 1) + count_set_bits(n >> 1)
    
n = 16
print(count_set_bits(n))



# Brian kernighan's Algorithm
def countSetBits(n):
    count = 0
    while (n):
        n &= (n-1) 
        count+= 1
    return count

i = 17
print(countSetBits(i))
 
