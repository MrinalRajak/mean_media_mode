

# Determination of mean , median , and mode of a given list of numbers

n=int(input("Enter the number of inputs: "))
a=[int(input())for i in range(n)]
mean = sum(a)/n
print("mean: ",mean)

for i in range(n):
    for j in range(n-i-1):
        if(a[j]>a[j+1]):
            a[j+1],a[j]=a[j],a[j+1]
if(n%2==0):
    median=(a[int(n/2-1)]+a[int(n/2)])/2
    print("median: ",median)
else:
    median=a[int((n-1)/2)]
    print("median: ",median)

maxcount=0
for i in range(n):
    count=0
    for j in range(n):
        if(a[i]==a[j]):
            count=count+1
    if(count>maxcount):
        maxcount=count
        maxnum=a[i]
print("The mode: ",maxnum)
print("Frequency of mode: ",maxcount)
