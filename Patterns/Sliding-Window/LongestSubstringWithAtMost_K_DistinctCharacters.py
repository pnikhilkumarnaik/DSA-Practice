def longest_k_distinct(s, k):

    left = 0
    maximum = 0

    frequency = {}

    for right in range(len(s)):

        frequency[s[right]] = (
            frequency.get(s[right], 0) + 1
        )

        while len(frequency) > k:

            frequency[s[left]] -= 1

            if frequency[s[left]] == 0:
                del frequency[s[left]]

            left += 1
        if right - left + 1 > maximum:
            maximum = right - left + 1
            res="".join(s[left:right + 1])

    return maximum,res


s = "ececceeecba"

print(longest_k_distinct(s, 2))

"""Output: (9, 'ececceeeec')

"""