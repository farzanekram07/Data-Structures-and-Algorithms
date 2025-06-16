# iterative approach
def multiplication(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i}")

n = int(input())
multiplication(n)


# recursion
def table(n, i=1):

    if i == 11:
        return
    print(n, "*", i, "=", n*i)
    i += 1
    table(n, i)

n = 5
table(n)
