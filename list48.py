# Write a Python program to split a given list into specified sized chunks.
#Original list:
#[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
#Split the said list into equal size 3
#[[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
#Split the said list into equal size 4
#[[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]
a=[12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
p=3
b=[]
i=0
while i<len(a):
    s=a[i:i+p]
    b.append(s)
    i=i+3
print(b,end="")    
