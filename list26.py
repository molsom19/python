#Our task is to print the element which occurs 3 consecutive times in a Python list.
#Example:
#Input: [4, 5, 5, 5, 3, 8]
#Output: 5
#Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
#Output: 1, 22
a=[4,5,5,5,3,8,]
p=[]
for i in range (0,len(a)):
    s=a[i]
    count=0
    for j in range (i,len(a)):
        k=a[j]
        if k==s:
            count=count+1
    if count>=3:
        p.append(s)
print(p)                