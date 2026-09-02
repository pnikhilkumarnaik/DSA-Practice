def min_subarray_len(target, arr):

    left = 0
    current_sum = 0
    subArray=[]

    minimum = float("inf")

    for right in range(len(arr)):

        current_sum += arr[right]

        while current_sum >= target:

            minimum = min(
                minimum,
                right - left + 1
            )
            subArray = arr[left:right + 1]

            current_sum -= arr[left]
            left += 1

    if minimum == float("inf"):
        return 0

    return minimum, subArray


arr = [2, 3, 1, 2, 4, 3]

print(min_subarray_len(7, arr))