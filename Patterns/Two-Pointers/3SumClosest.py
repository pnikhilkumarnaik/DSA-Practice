def three_sum_closest(arr, target):

    arr.sort()

    closest = arr[0] + arr[1] + arr[2]
    indexs=[]
    for i in range(len(arr) - 2):
       
        left = i + 1
        right = len(arr) - 1

        while left < right:

            total = arr[i] + arr[left] + arr[right]

            if abs(target - total) < abs(target - closest):
                indexs=[]
                closest = total
                indexs=[i,left,right]

            if total < target:
                left += 1

            elif total > target:
                right -= 1

            else:
                indexs=[i,left,right]
                return total,indexs

    return closest,indexs


arr = [-1, 2, 1,-4]

print(three_sum_closest(arr, 1))
print(arr)

"""Output:
(2, [0, 1, 2])
"""