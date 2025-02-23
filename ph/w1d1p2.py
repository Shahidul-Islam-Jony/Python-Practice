
a,b,c = map(int,(input('Enter three number:')).split())

# print(abs(a))
# print(abs(b))
# print(abs(c))

def custAbs(n):
    if n>0:
        return n
    else:
        return -n
    
print(custAbs(a))
print(custAbs(b))
print(custAbs(c))