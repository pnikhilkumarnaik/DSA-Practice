def longest_subarray_sum_k(arr, k):

    prefix_sum = 0
    maximum = 0

    first_index = {}

    for i, num in enumerate(arr):

        prefix_sum += num

        if prefix_sum == k:
            maximum = i + 1

        if prefix_sum - k in first_index:

            length = i - first_index[prefix_sum - k]

            maximum = max(maximum, length)

        if prefix_sum not in first_index:
            first_index[prefix_sum] = i

    return maximum


arr = [10, 5, 2, 7, 1, 9]

print(longest_subarray_sum_k(arr, 15))

"""
OutPUt: 4

"""