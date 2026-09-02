def running_sum(arr):
    prefix = []

    total = 0

    for num in arr:
        total += num
        prefix.append(total)

    return prefix



arr = [1, 2, 3, 4]

print(running_sum(arr))

"""Output: [1, 3, 6, 10]

"""