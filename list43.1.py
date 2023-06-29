a=['s','d','f','j','s','a','j','d','f','d']
letters=input("enter letter")
i=3
while i<len(a):
    a.insert(i,letters)
    i=i+4
print(a)    