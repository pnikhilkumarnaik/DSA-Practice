def four_sum(arr, target):

    arr.sort()

    result = []
    n = len(arr)

    for i in range(n - 3):

        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, n - 2):

            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:

                total = (
                    arr[i]
                    + arr[j]
                    + arr[left]
                    + arr[right]
                )

                if total == target:

                    result.append([
                        arr[i],
                        arr[j],
                        arr[left],
                        arr[right]
                    ])

                    left += 1
                    right -= 1

                elif total < target:
                    left += 1

                else:
                    right -= 1

    return result


arr = [1, 0, -1, 0, -2, 2]

print(four_sum(arr, 0))

"""
Output:
[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
"""