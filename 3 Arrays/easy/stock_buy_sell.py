
def buy_and_sell(arr):
    n = len(arr)

    for i in range(n):
        current_max = arr[i]
        if current_max < arr[i]:
            buy = current_max
        
