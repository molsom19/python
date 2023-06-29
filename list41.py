a=[3.2,8,9.9,4.2,5,0.1]
n=input("enter no")
n=float(n)
p=[]
i=0
while i<len(a):
    s=a[i]+n
    p.append(s)
    i=i+1
print(p)    