def frequency(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    return freq


arr = [1, 2, 2, 3, 3, 3]

print(frequency(arr))

#or

d={}
for num in arr:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

print(d)

"""Output:

{1: 1, 2: 2, 3: 3}
"""