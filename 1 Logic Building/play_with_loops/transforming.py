# Want: Only unique unordered pairs where the sum is even
# Then: Transform to string: "Pair: (a, b), Sum: s"

# # my_writing
# def generating_pairs_with_filter_and_transformation(arr):
#     new_arr = []
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] < arr[j] and (arr[i] + arr[j]) % 2 == 0:
#                 new_arr.append([arr[i],arr[j]])
    
#     for (a,b) in new_arr:
#         print(f"{a} + {b} = {a+b}")
#     return new_arr

# arr = [1, 2, 3, 4]
# print(generating_pairs_with_filter_and_transformation(arr))



# # optimal
# def generating_filtering_transforming(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             a = arr[i]; b = arr[j]
#             if (a + b) % 2 == 0:
#                 print(f"{a} + {b} == {a + b}")
                
# arr = [1, 2, 3, 4]
# generating_filtering_transforming(arr)



# # list comprehension
# def generating_transforming(arr):
#     return [
#         f"{a} + {b} = {a + b}"
#         for i in range(len(arr))
#         for j in range(i+1, len(arr))
#         if (a := arr[i]) + (b := arr[j]) % 2 == 0
#     ]

# arr = [1, 2, 3, 4]
# print(generating_transforming(arr))




# Functional Separation (Extra clean style)
def generate_pairs(arr):
    return [(arr[i], arr[j]) for i in range(len(arr)) for j in range(i+1, len(arr))]

def filtered_even_sum(pairs):
    return [pair for pair in pairs if (sum(pair) % 2) == 0]

def transform_pairs(pairs):
    return [f"{a} + {b} = {a + b}" for a, b in pairs]

def filtered_absolute_difference(pairs):
    return [pair for pair in pairs if abs(pair[0] - pair[1]) == 1]

def transform_into_dictionary(pairs):
    return [f"{a}, {b} : {abs(a-b)}" for a, b in pairs]

arr = [1, 2, 3, 4]
pairs = generate_pairs(arr)
filtered = filtered_even_sum(pairs)
transform = transform_pairs(filtered)
difference = filtered_absolute_difference(pairs)
dictionary = transform_into_dictionary(difference)
print("All pairs:", pairs)
print("Filtered even pairs:", filtered)
print("\n".join(transform))
print("Filtered absolute difference:", difference)
print("\n".join(dictionary))
