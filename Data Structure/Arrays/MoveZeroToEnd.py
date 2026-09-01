def move_zeros(arr):
    j = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr


arr = [0, 1, 0, 3, 12]

print(move_zeros(arr))
"""Output:      
[1, 3, 12, 0, 0]
"""