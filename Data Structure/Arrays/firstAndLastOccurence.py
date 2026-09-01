def first_occurrence(arr, target):

    left = 0
    right = len(arr) - 1
    answer = -1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            answer = mid
            right = mid - 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return answer


def last_occurrence(arr, target):

    left = 0
    right = len(arr) - 1
    answer = -1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            answer = mid
            left = mid + 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return answer


arr = [1, 2, 2, 2, 3, 4]

print(first_occurrence(arr, 2))
print(last_occurrence(arr, 2))

"""Output:  
0
3
"""