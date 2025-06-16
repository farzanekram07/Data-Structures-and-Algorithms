#1 Nested Loops & Generating Pairs
print("First problem")
for i in range(5):
    for j in range(5):
        print([i, j], end = ' ')
    print()
print()

#2 Generate only pairs where i < j 
# (to avoid duplicates like (2,1) 
# when (1,2) already exists)
print("Second problem")
for i in range(5):
    for j in range(5):
        if i == j:
            print([i,j], end = ' ')
        if i < j or i > j:
            print(['-', '-'], end = " ")
    print()
print()

for i in range(5):
    for j in range(5):
        if i == j:
            print([i,j], end=' ')
        else:
            print("       ", end=' ')  
    print()
