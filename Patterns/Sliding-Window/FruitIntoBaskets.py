def total_fruits(arr):

    left = 0
    maximum = 0

    frequency = {}

    for right in range(len(arr)):

        frequency[arr[right]] = (
            frequency.get(arr[right], 0) + 1
        )

        while len(frequency) > 2:

            frequency[arr[left]] -= 1

            if frequency[arr[left]] == 0:
                del frequency[arr[left]]

            left += 1
        if right - left + 1 > maximum:
            maximum = right - left + 1
            res = arr[left:right + 1]
       

    return maximum,res


arr = [1, 2, 1, 2, 3]

print(total_fruits(arr))

"""

Output: (4, [1, 2, 1, 2])

"""