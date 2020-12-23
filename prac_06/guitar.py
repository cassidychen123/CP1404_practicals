CURRENT_YEAR = 2017
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, cost=0, name="", year=0):
        self.cost = cost
        self.name = name
        self.year = year

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        return self.year < other.year