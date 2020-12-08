"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9.0 * (fahrenheit - 32)
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

def celsius(fahrenheit):
    return (fahrenheit-32)*5/9.0
fahrenheit = float(input("Fahrenheit: "))
print(celsius(fahrenheit))

def fahrenheit(celsius):
    return (celsius-32)*5/9.0
celsius = float(input("Celsius: "))
print(fahrenheit(celsius))

