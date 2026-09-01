def max_water(height):

    left = 0
    right = len(height) - 1

    maximum = 0

    while left < right:

        width = right - left

        current = min(
            height[left],
            height[right]
        ) * width

        maximum = max(maximum, current)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maximum


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(max_water(height))

"""
Output: 49
"""