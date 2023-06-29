from os import P_WAIT


a=[5,6,[],3,[],[],9]
i=0
P=[]
while i<len(a):
    if type(a[i])==list:
        pass
    else:
        P.append(a[i])
    i=i+1
print(P)               