a=[-12,14,95,3]
i=0
pos_count=0
neg_count=0
while i<len(a):
    if 0<=a[i]:
        pos_count=pos_count+1
    else:
        neg_count=neg_count+1
    i=i+1
print("pos_count=",pos_count)
print("neg_count=",neg_count)               

