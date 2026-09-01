def move_zeros(arr):

    slow = 0

    for fast in range(len(arr)):

        if arr[fast] != 0:

            arr[slow], arr[fast] = arr[fast], arr[slow]

            slow += 1

    return arr


arr = [0, 1, 0, 3, 12]

print(move_zeros(arr))

"""Output:      
[1, 3, 12, 0, 0]
"""