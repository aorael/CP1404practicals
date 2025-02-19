"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    total_month = int(input("How many months? "))
    incomes = get_income(incomes, total_month)
    display_income(incomes, total_month)

def get_income(incomes, total_month):
    incomes = []
    for month in range(1, total_month + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)
    return incomes


def display_income(incomes, total_month):
    """Printing income report"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, total_month + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()