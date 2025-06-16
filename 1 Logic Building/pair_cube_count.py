# Given n, count all ‘a’ and ‘b’ that satisfy 
# the condition a^3 + b^3 = n. Where (a, b) 
# and (b, a) are considered two different pairs


# brute force - O(N2)
def cube_pair_count(n):
    count = 0
    new_arr = []
    for i in range(n):
        for j in range(n):
            if i ** 3 + j ** 3 == n:
                new_arr.append([i,j])
                count += 1
    return new_arr, count

n = 9
print(cube_pair_count(n))




# If a³ > n, then adding b³ will only 
# increase it, making it useless.


# limited brute force - O(N(2/3))
def pair_count(n):
    count = 0
    new_arr = []
    limit = int(n ** (1/3)) + 1
    for i in range(limit):
        for j in range(limit):
            if i ** 3 + j ** 3 == n:
                new_arr.append([i,j])
                count += 1
    return new_arr, count

n = 9
print(pair_count(n))




# a³ + b³ = n  ➝  b³ = n - a³
# So if we loop over all a, we can 
# calculate b³ as n - a³, and then check:
# “Is b³ a perfect cube? If yes, 
# then we found a pair (a, b).”


# fully optimized - O(N(1/3))
def count_of_cubic_pair(n):
    count = 0
    new_arr = []
    limit = int(n ** (1/3)) + 1
    for a in range(limit):
        a_cubed = a ** 3
        b_cubed = n - a_cubed
        if b_cubed < 0:
            continue  # skip negative cubes
        b = round(b_cubed ** (1/3))
        if b ** 3 == b_cubed:
            new_arr.append([a,b])
            count += 1
            # if a != b:
            #     new_arr.append([b,a])
            #     count += 1
    return new_arr, count

n = 9
print(count_of_cubic_pair(n))