def pair_difference(arr, target):

    arr.sort()

    left = 0
    right = 1

    while right < len(arr):

        difference = arr[right] - arr[left]

        if difference == target:
            return True,left,right

        elif difference < target:
            right += 1

        else:
            left += 1

            if left == right:
                right += 1

    return False


arr = [1, 5, 3, 4, 2]

print(pair_difference(arr, 2))

"""Output: (True, 0, 2)

"""