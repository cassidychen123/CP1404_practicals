finished = False
result = 0
while not finished:
    try:
        result = int(input("enter a integer:"))
        finished = True
    except ValueError as error:
        print("Please enter a valid integer.")
print("Valid result is:", result)