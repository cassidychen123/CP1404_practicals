def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month: {}".format(month)))
        incomes.append(income)

    print_report(incomes)

def print_report(incomes):
    total = 0
    print("\nIncome Report\n-------------")
    for month, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()