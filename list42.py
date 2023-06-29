42.# Write a Python program to iterate a given list cyclically on specific index position.
#Original list:
#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#Iterate the said list cyclically on specific index position 3 :
#['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
#Iterate the said list cyclically on specific index position 5 :
#['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']
a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
p=[]
n=int(input("enter no"))
for i in range (n,len(a)):
    p.append(a[i])
for j in range (0,n):
    p.append(a[j])
print(p)

        
