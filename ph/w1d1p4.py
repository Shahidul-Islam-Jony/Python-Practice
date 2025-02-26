
while True:
    value = input('Enter a value :')
    if(value.lower()=='quit'):
        break

    number= int(value)
    if(number>0):
        print('Positive number')
    elif number<0:
        print('Negative number')
    else:
        print('Zero')
