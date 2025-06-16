#1 print even numbers from 2 to 20
for i in range(2, 21):
    print(i, end = " ")
print()

## print even
for i in range(2, 21):
    if i % 2 == 0:
        print(i, end = " ")
print()

## using list comprehension
print([i for i in range(2, 21) if i % 2 == 0])




#2 print numbers from 10 to 1 (reverse)
for i in range(10, 0, -1):
    print(i, end = " ")
print()
