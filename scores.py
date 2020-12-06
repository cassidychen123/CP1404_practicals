import random
def ran(score):
    if 0 < score < 100:
        if score > 90:
            print("Excellent")
        if 50 < score <= 90:
            print("Passable")
        if score < 50:
            print("Bad")
    else:
        print("Invalid score")

def main():
    score = random.randint(0, 100)
    print('{} is {}'.format(score, ran(score)))
    file = open("results.txt", "w")
    file.write('{} is {}'.format(score, ran(score)))

main()

