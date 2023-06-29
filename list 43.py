a=[1,3,5,7,9,11,0,2,4,6,8,10,8,9,0,4,3,0]
n=int(input("enter no"))
i=4
while i<len(a):
    a.insert(i,n)
    i=i+5
print(a)

