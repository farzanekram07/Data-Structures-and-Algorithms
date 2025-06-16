#1 Generate all ordered pairs from a arr: a = [1, 2, 3]
def pairs(arr):
    result = []
    for i in arr:
        for j in arr:
            result.append([i, j])
    return result

arr = [1, 2, 3]
print(pairs(arr))


#2 Generate all combinations where i != j from the same list

# def pairs1(arr):
#     for i in arr:
#         for j in arr:
#             if i != j:
#                 print([i,j], end= " ")
#     print()

# arr = [1, 2, 3]
# pairs1(arr)


a =  pairs(arr)
for i in a:
    if i[0] != i[1]:
        print(i, end = " ")
print()


#3 Count how many pairs are generated where i < j
count = 0
for i in a:
    if i[0] < i[1]:
        count += 1
print(count)




# More pythonic way
# arr = [1, 2, 3]
# all_pairs = [[i, j] for i in arr for j in arr]
# filtered_pairs = [pair for pair in all_pairs if pair[0] != pair[1]]
# count_lt = sum(1 for pair in all_pairs if pair[0] < pair[1])

# print("All pairs:", all_pairs)
# print("Filtered (i != j):", filtered_pairs)
# print("Count where i < j:", count_lt)





# More functional way
def generate_pairs(arr):
    return [[i, j] for i in arr for j in arr]
def filter_not_equal(pairs):
    return [pair for pair in pairs if pair[0] != pair[1]]
def count_less_than(pairs):
    return sum(1 for pair in pairs if pair[0] < pair[1])

arr = [1, 2, 3]

all_pairs = generate_pairs(arr)
print("All pairs:", all_pairs)

filtered_pairs = filter_not_equal(all_pairs)
print("Filtered (i != j):", filtered_pairs)

count_lt = count_less_than(all_pairs)
print("Count where i < j:", count_lt)
