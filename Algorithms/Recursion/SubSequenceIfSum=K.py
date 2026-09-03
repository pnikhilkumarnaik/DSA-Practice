arr=[1,2,1]
l=len(arr)
def subsequence_if_sum_k(n,subseq,sum,k): 
    if n==l:
        if sum==k:
            print(subseq)
        return
    subseq.append(arr[n])
    sum+=arr[n]
    subsequence_if_sum_k(n+1,subseq,sum,k)
    subseq.pop()
    sum-=arr[n]
    subsequence_if_sum_k(n+1,subseq,sum,k)

    return

subsequence_if_sum_k(0,[],0,2)

"""
output: [1, 1]
        [2]     
        
        """

arr=[1,2,1]
l=len(arr)
k=2
def sub(n,s,sa,k):
    if n==l:
        if s==k:
            print(sa)
            return True
        else:
            return False
    s+=arr[n]
    sa.append(arr[n])
    if sub(n+1,s,sa,k)==True:
        return True
    s-=arr[n]
    sa.remove(arr[n])
    
    if sub(n+1,s,sa,k)==True:
        return True
    
    return False
sub(0,0,[],k=2 )

"""
OUTPUT: [1, 1]
"""
    
         
