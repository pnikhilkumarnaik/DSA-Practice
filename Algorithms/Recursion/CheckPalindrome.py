s="madam"

def is_palindrome(left,right):
    if left>=right:
        return True

    if s[left]!=s[right]:
        return False
    
    return is_palindrome(left+1,right-1)
print(is_palindrome(0,len(s)-1))

"""
OUTPUT: True
"""
