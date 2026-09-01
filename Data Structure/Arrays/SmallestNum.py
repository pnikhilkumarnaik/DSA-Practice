def two_smallest(arr):
    smallest = float("inf")
    second = float("inf")

    for num in arr:
        if num < smallest:
            second = smallest
            smallest = num

        elif num < second and num != smallest:
            second = num

    return smallest, second


arr = [5, 2, 8, 1, 4]
smallest, second = two_smallest(arr)
print(f"First smallest number: {smallest}")
print(f"Second smallest number: {second}")

"""Output:
First smallest number: 1
Second smallest number: 2
"""