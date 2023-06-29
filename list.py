a=[20,37,20,21]
b=[]
for i in range(0,len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)    