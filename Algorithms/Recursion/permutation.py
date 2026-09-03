def permutations(arr):

    result = []

    def backtrack(current, used):

        if len(current) == len(arr):
            result.append(current.copy())
            return

        for i in range(len(arr)):

            if used[i]:
                continue

            # Make choice
            used[i] = True
            current.append(arr[i])

            # Explore
            backtrack(current, used)

            # Undo choice
            current.pop()
            used[i] = False

    backtrack([], [False] * len(arr))

    return result


print(permutations([1, 2, 3]))


"""
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""