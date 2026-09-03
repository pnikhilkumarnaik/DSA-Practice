arr=[1,2,3 ]
l=len(arr)
def all_subsequences(arr,n,subseq):
    if n==l:
        print(subseq)
        return 
    subseq.append(arr[n])
    all_subsequences(arr,n+1,subseq)
    subseq.pop()
    all_subsequences(arr,n+1,subseq)        

    return
all_subsequences(arr,0,[])