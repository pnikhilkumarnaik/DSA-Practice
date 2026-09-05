def max_profit(jobs, i):

    if i == len(jobs):
        return 0
   
    next_i = i + 1

    while next_i < len(jobs) and jobs[next_i][0] < jobs[i][1]:
        next_i += 1

    take = jobs[i][2] + max_profit(jobs, next_i)
    skip = max_profit(jobs, i + 1)

    return max(take, skip)

jobs = [
    (1, 3, 50),
    (2, 5, 20),
    (4, 6, 70),
    (6, 7, 60)
]

print("Maximum Profit:", max_profit(jobs, 0))

"""
Output: Maximum Profit: 120
"""