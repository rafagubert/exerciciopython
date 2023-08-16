numbers = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four'
}
phone = input("Phone: ")
output = ''
for number in phone:
    output += numbers.get(number, 'Invalid Number') + ' '

print(output)


