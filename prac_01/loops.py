#c
def main():
    length = int(input("Number of stars:"))
    for i in range (length):
        for j in range (i + 1):
            print("*", end='')
        print("\n")

main()

#a
for a in range (0, 101, 10):
    print(a, end=' ')

#b
for b in range(20, 0, -1):
    print(b, end=' ')
print()