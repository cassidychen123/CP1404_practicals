numbers = [3, 1, 4, 1, 5, 9, 2]

# 1
numbers[0] = "10"
print(numbers)
# 2
numbers[-1] = '1'
print(numbers)
# 3
del numbers[2:]
print(numbers)
# 4
if '9' in numbers:
    print('9 is in numbers')
else:
    print('9 is not in numbers')