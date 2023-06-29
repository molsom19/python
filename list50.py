50. #Write a Python program to join two given list of lists of same length, element wise.
#Original lists:
#[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
#[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
#Join the said two lists element wise:
#[[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
a=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
b=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
p=[]
i=0
while i<len(a):
    j=0
    while j<1:
        p.append(a[i]+b[i])
        j=j+1
    i=i+1
print(p)