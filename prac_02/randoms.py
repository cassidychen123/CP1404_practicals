import random
print(random.randint(5, 20))  # minimum:5 maximum:20
print(random.randrange(3, 10, 2))  # minimum:3 maximum:9 cannot produce 4, because the step is 2.
print(random.uniform(2.5, 5.5))  # minimum: 2.507537508357972 maximum:5.

print(random.randint(0, 100))