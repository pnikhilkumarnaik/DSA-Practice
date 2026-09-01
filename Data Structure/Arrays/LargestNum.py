def largest(arr):

    large = float('-inf')
    second = float('-inf')

    for num in arr:
        if num >= large:
            large = num
        elif num >second and num != large :
            second=num 

    return large,second


arr = [10, 25, 3, 78, 45]
largest_num, second_largest = largest(arr)
print(f"Largest number: {largest_num}")
print(f"Second largest number: {second_largest}")

""" OUTPUT:
Largest number: 78
Second largest number: 45
"""