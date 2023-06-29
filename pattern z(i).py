i=0
while i<5:
    j=0
    while j<5:
        if i+j==2 or i+j==6 or i-j==2 or j-i==2:
            print(" * ",end="  ")
        else:
            print("  ",end="  ")
        j=j+1
    print()
    i=i+1
        