numbers = []
i = 0
for i in range(5):
    numbers.append(int(input("Number :"(i+1))))
print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))

def ave(numbers):
    sum = 0
    for j in numbers:
        sum += j
    return sum/5
print("The average of the numbers is", ave(numbers))


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
newnames = usernames.copy()
name = str(input("please enter your name:"))
if name in usernames:
    print("Access granted")
else:
    print("Access denied")


