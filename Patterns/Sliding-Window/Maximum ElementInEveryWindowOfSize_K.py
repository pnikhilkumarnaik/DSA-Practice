from collections import deque


def max_sliding_window(arr, k):

    dq = deque()
    result = []

    for right in range(len(arr)):

        # Remove smaller elements
        while dq and arr[dq[-1]] <= arr[right]:
            dq.pop()

        dq.append(right)

        # Remove elements outside window
        if dq[0] <= right - k:
            dq.popleft()

        # Window is ready
        if right >= k - 1:
            result.append(arr[dq[0]])

    return result


arr = [1, 3, -1, -3, 5, 3, 6, 7]

print(max_sliding_window(arr, 3))

"""Output: [3, 3, 5, 5, 6, 7]
"""