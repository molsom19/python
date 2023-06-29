a=[6,1,3,5,6,3,1]
i=0
p=[]
product=1
for i in range (0,len(a)):
    if a[i] not in p:
        p.append(a[i])
        product=product*(a[i])
print(product)        