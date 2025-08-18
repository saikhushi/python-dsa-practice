n=int(input())
resultBinaryString=""
while(n!=0):
    rem=n%2
    resultBinaryString+=str(rem)
    n=n//2
print(resultBinaryString[::-1])