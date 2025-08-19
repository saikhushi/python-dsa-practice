arr=list(map(int,input().split()))
n=len(arr)
total_subsets=(1<<n)
ans=[]
for val in range(total_subsets):
    subset=[]
    for i in range(n):
        if(val&(1<<i)):
            subset.append(arr[i])
    ans.append(subset)
print(ans)