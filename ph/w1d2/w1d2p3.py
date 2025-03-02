
prev= 0
current = 1

print(0, 1, end=" ")

for i in range(2,10):
    print(prev+current,end=" ")
    temp=current
    current=prev+current
    prev=temp
