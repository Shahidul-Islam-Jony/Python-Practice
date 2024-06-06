# string operations

first_name = "Shahidul"
# print(len(first_name))
last_name = "Islam"
age = 25

full_name = first_name +' '+last_name
# print(full_name)

# print(first_name[0])

text = f'My name is {first_name} {last_name} . I am {age} years old.'
# print(text)

# for letter in first_name:
#     # print(letter)       // print letter seperate line
#     print(letter,end=' ')  // print letter same line

# print(len(last_name))


a = """lorem ipsum 
200"""       #Multi Line string 
# print(a)

txt = "The best thing is not free in life"

# print('free' in txt)      # return true

# print('Expensive' not in txt)   # return true

item_no = 1505
quantity = 10

# myOrder = "I need item_no {} to {} piece"
# print(myOrder.format(item_no,quantity))

myOrder = "I need item_no {1} to {0} piece"
# print(myOrder.format(quantity,item_no))   # you can set by indexing




