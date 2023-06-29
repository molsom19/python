num=[50,40,23,70,56,12,5,10,7]
i=0
max=0
s_max=0
while i<len(num):
    if num[i]>max:
        s_max=max
        max=num[i]
    elif num[i]>s_max:
        s_max=num[i]
    i=i+1
print("secound ma=",s_max)