r=1
while r<=5:
    c=1
    while c<=5:
        if r==1 or c==3:
            print(" * ",end=" ")
        else:
            print("   ",end=" ")
        c=c+1
    print()
    r=r+1
        