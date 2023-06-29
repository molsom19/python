a=[12,67,98,34]
b=[]
i=0
while i<len(a):
    p=str(a[i])
    sum=0
    j=0
    while j<len(p):
        s=int(p[j])
        sum=sum+s
        j=j+1
    b.append(sum)
    i=i+1
print(b)           