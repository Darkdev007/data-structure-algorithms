# num1 = 11
# num2 = num1

# print(f'The value of num1 is {num1}')
# print(f'The value of num2 is {num2}')

# num1 = 22
# print(f'The value of num1 is {num1}')
# print(f'The value of num2 is {num2}')

dict1 = {
    'value' : 22
}
dict3 = {
    'value' : 88
}
dict2 = dict1

print(f'The value of dict1 is {dict1}')
print(f'The value of dict2 is {dict2}')

dict1['value'] = 44

print(f'The value of dict1 is {dict1}')
print(f'The value of dict2 is {dict2}')

dict2 = dict3
print(f'The value of dict2 is {dict2}')
print(f'The value of dict3 is {dict3}')

dict1 = dict3
print(f'The value of dict2 is {dict2}')
print(f'The value of dict3 is {dict3}')
print(f'The value of dict1 is {dict1}')
