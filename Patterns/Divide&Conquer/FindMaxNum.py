def find_max(arr, left, right):

    if left == right:
        return arr[left]

    mid = (left + right) // 2

    left_max = find_max(arr, left, mid)
    right_max = find_max(arr, mid + 1, right)

    return max(left_max, right_max)


arr = [8, 3, 10, 5, 2, 7]

print(find_max(arr, 0, len(arr) - 1))

"""
Output: 10
"""