def max_product(arr):

    current_max = arr[0]
    current_min = arr[0]

    result = arr[0]

    for num in arr[1:]:

        if num < 0:
            current_max, current_min = current_min, current_max

        current_max = max(
            num,
            current_max * num
        )

        current_min = min(
            num,
            current_min * num
        )

        result = max(result, current_max)

    return result


arr = [2, 3, -2, 4]

print(max_product(arr))

"""
Output:6
"""