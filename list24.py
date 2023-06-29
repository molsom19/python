a=[1,2,3,1,2,2]
b=[]
for i in range (0,len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)