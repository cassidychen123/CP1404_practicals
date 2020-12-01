def main():
    num = int(input("how many items do you have?"))
    total = 0
    i = 0
    for i in range(num):
        price =float(input("Price of items:"))
        total += price
        if total >100:
            final = 0.9 * total
        else:
            final = total
    print("Total price for",num, "items is $", final)

main()