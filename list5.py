a=[1,2,2,5,8,4,4,8]
p=[]
count=0
for i in range (0,len(a)):
    if a[i] not in p:
        p.append(a[i])
        count=count+1
print("uniqe value:",count)