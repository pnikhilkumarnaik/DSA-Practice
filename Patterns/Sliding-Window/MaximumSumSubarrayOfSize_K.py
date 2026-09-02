def max_sum_k(arr, k):

    window_sum = sum(arr[:k])
    maximum = window_sum

    for right in range(k, len(arr)):

        window_sum += arr[right]
        window_sum -= arr[right - k]

        maximum = max(maximum, window_sum)

    return maximum


arr = [2, 1, 5, 1, 3, 2]

print(max_sum_k(arr, 3))

"""
Output: 9
"""