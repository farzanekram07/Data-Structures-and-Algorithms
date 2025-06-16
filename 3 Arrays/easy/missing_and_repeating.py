# # iterative - O(N)| O(N)

# def missing(arr):
#     n = len(arr)

#     freq = [0] * (n+1)
#     missing = -1
#     repeating = -1

#     for i in range(n):
#         freq[arr[i]] += 1
    
#     return freq

# arr = [1, 1, 2, 3, 2, 1, 1, 3]
# print(missing(arr))



# Python program to find Missing 
# and Repeating in an Array

def findTwoElement(arr):
    n = len(arr)

    # Creating frequency list of size n+1 with
    # initial values as 0. Note that array
    # values will go upto n, that is why we 
    # have taken the size as n+1
    freq = [0] * (n + 1)
    repeating = -1
    missing = -1

    # Find the frequency of all elements.
    for i in range(n):
        freq[arr[i]] += 1

    # for i in range(1, n + 1):

    #     # For missing element, frequency
    #     # will be 0.
    #     if freq[i] == 0:
    #         missing = i

    #     elif freq[i] == 2:
    #         repeating = i

    return freq

if __name__ == "__main__":
    arr = [3, 1, 3]
    ans = findTwoElement(arr)

    print(ans)





## my piece of code for understanding
def missing_number(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        
    duplicate = []
    for num in freq:
        if freq[num] > 1:
            duplicate.append(num)

    missing = []
    for num in range(1, max(arr) + 1):
        if num not in freq:
            missing.append(num)
    
    print("Duplicates: ", duplicate)
    print("Missing: ", missing)



arr = [2, 3, 5, 6, 9, 3, 2, 2]
missing_number(arr)





# By comparing the actual sum and square sum, 
# you can derive the missing and repeating numbers.
def find_missing_and_duplicate_math(arr):
    n = len(arr)
    
    expected_sum = n * (n + 1) // 2
    expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6

    actual_sum = sum(arr)
    actual_sq_sum = sum(x * x for x in arr)

    # Let:
    #   x = missing number
    #   y = duplicate number
    #
    # Equations:
    #   x - y = expected_sum - actual_sum
    #   x^2 - y^2 = expected_sq_sum - actual_sq_sum
    # => (x + y)(x - y) = diff_square

    diff = expected_sum - actual_sum                # x - y
    diff_square = expected_sq_sum - actual_sq_sum   # x^2 - y^2

    # (x + y) = diff_square / diff
    sum_xy = diff_square // diff

    # Now solve:
    # x = (diff + sum_xy) / 2
    # y = x - diff
    x = (diff + sum_xy) // 2
    y = x - diff

    return y, x  # duplicate, missing

arr = [4, 1, 2, 2, 5]
print(find_missing_and_duplicate_math(arr))
