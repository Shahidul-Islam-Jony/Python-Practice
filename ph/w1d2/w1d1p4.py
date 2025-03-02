char = input('Enter any character with number and symbol :')

uppercase=0
lowercase=0
digits=0
symbol=0

for ch in char:
    if (ch>='a' and ch<='z'):
        lowercase+=1
    elif(ch>='A' and ch<='Z'):
        uppercase+=1
    elif(ch>='0' and ch<='9'):
        digits+=1
    else:
        symbol+=1

print("Uppercase = ",uppercase)
print("Lowercase = ",lowercase)
print('Digits = ',digits)
print('Symbol = ',symbol) 