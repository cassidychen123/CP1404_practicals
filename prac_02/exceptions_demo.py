"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
input sting or float, what is more, when demominator is 0, valueError will occur.
2. When will a ZeroDivisionError occur?
when numerator and denominator are all 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")