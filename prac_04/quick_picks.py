import random

def main():
    get_number = int(input("How many quick picks? "))
    while get_number < 0:
        print("That makes no sense!")
        get_number = int(input("How many quick picks? "))

    for i in range(get_number):
        quick_picks = []
        for j in range(6):
            number = random.randint(1, 45)
            while number in quick_picks:
                number = random.randint(1, 45)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join("{:2}".format(number) for number in quick_picks))
main()