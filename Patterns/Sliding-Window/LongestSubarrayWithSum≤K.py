def longest_subarray(arr, k):

    left = 0
    current_sum = 0
    maximum = 0

    for right in range(len(arr)):

        current_sum += arr[right]

        while current_sum > k:

            current_sum -= arr[left]
            left += 1

        maximum = max(
            maximum,
            right - left + 1
        )

    return maximum


arr = [2, 1, 1, 3, 2, 1]

print(longest_subarray(arr, 5))

"""Output: 3
"""

