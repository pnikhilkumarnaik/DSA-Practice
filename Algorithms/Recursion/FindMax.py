arr=[2,5,7,9,3]
l=len(arr)-1
def find_max(arr,n):
    if n==l:
        return arr[n]
    curr=find_max(arr,n+1)
    return max(curr,arr[n])

print(find_max(arr,0))

"""Output: 9
"""