def rotate(arr, k):
    n = len(arr)

    k = k % n

    arr[:] = arr[-k:] + arr[:-k]

    return arr


arr = [1, 2, 3, 4, 5]

print(rotate(arr, 2))
"""Output:
[4, 5, 1, 2, 3]
"""