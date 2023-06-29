a=[34.67,-94.89,12,'python',0,'c#']
i=0
s=[]
while i<len(a):
    p=a[i]
    if type(p)==str:
        s.append(p)
    i=i+1
print(s)        
