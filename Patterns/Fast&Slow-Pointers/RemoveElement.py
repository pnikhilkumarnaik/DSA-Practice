def remove_element(arr, val):

    slow = 0

    for fast in range(len(arr)):

        if arr[fast] != val:

            arr[slow] = arr[fast]
            slow += 1

    return slow


arr = [3, 2, 2, 3]

length = remove_element(arr, 3)

print(arr[:length])

"""
Output:  [2, 2]
"""