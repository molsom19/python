a=['red','maroon','yellow','olive']
i=0
p=[]
while i<len(a):
    j=0
    k=[]
    while j<len(a[i]):
        k.append(a[i][j])
        j=j+1
    i=i+1
    p.append(k)
print(p)        