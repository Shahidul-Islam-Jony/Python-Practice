
value = input('Enter a string with mixed upper and lower case:')

# print(value)

output=''

for val in value:
    if (val>='A' and val<='Z'):
        output+=val.lower()
    else:
        output+=val.upper()

print(output)
