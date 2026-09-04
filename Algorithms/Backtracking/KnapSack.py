def knapsack(weights, profits, capacity, index, current_weight, current_profit):

    # Base case
    if index == len(weights):
        return current_profit

    # Choice 1: Take the item
    take = 0

    if current_weight + weights[index] <= capacity:
        take = knapsack(
            weights,
            profits,
            capacity,
            index + 1,
            current_weight + weights[index],
            current_profit + profits[index]
        )

    # Choice 2: Don't take the item
    skip = knapsack(
        weights,
        profits,
        capacity,
        index + 1,
        current_weight,
        current_profit
    )

    # Return maximum profit
    return max(take, skip)


weights = [2, 3, 4]
profits = [40, 50, 60]

capacity = 5

answer = knapsack(
    weights,
    profits,
    capacity,
    0,
    0,
    0
)

print("Maximum Profit:", answer)

"""
Output: Maximum Profit: 90
"""