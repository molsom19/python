a=['1','2','3','4','5','6']
i=0
p=[]
while i<len(a):
    j=i+1
    while j<len(a):
        p.append(a[i]+a[j])
        j=j+len(a)
    i=i+2
print(p)    