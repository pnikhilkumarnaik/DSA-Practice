def remove_duplicates(arr):

    if len(arr) == 0:
        return 0

    slow = 0

    for fast in range(1, len(arr)):

        if arr[fast] != arr[slow]:

            slow += 1
            arr[slow] = arr[fast]

    return slow + 1


arr = [1, 1, 2, 2, 3, 4, 4]

length = remove_duplicates(arr)

print(arr[:length])

"""Output:
[1, 2, 3, 4]
"""