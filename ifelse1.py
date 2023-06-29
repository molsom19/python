# a=int(input("enter number"))
# b=int(input("enter number"))
# if a>b:
#     print("a is maximum")
# elif b>a:
#     print("b is maximum")
# else:
#     print("none")        





a= int(input("Enter any no"))
b= int(input("Enter any no"))
c= int(input("Enter any no"))
d=0
if a>b:
    if a>c:
        d=a 
elif b>a:
    if b>c:
        d=b
else:
    d=c
print(d)
