def longest_unique_substring(s):

    left = 0
    maximum = 0
    
    seen = set()

    for right in range(len(s)):

        while s[right] in seen:

            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        if right - left + 1 > maximum:
       
            maximum = right - left + 1
            res="".join(s[left:right + 1])

    return maximum,res


s = "abcabdcbb"

print(longest_unique_substring(s))

"""
Output: (4, 'cadb')

"""