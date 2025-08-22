row=int(input())
ans=1
print(ans,end=" ")
for col in range(1,row):
    ans=ans*(row-col)
    ans=ans//(col)
print(ans,end=" ")
