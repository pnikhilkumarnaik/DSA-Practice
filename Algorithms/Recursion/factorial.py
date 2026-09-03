n=5
def fac(n):
    if n==0:
        return 1
    n=n*fac(n-1)
    return n
print(fac(n))   

"""

Output: 120
"""