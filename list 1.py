#convert character matrix to single string:
#the original list is:[['g','f','g']['i','s']['b','e','s','t']]
a=[['g','f','g'],['i','s'],['b','e','s','t']]
i=0
p=""
while i<len(a):
    j=0
    while j<len(a[i]):
        k=a[i][j]
        p=p+k
        j=j+1
    i=i+1
print(p)                                      