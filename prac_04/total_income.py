"""

  incomes ← []
  months ← INPUT("How many months? ")
  FOR month ← 1 TO months DO
    income ← INPUT("Enter income for month " + month + ": ")
    APPEND income TO incomes
  CALL print_report(incomes)

FUNCTION print_report(incomes)
  PRINT "Income Report"
  total ← 0
  FOR month ← 1 TO LENGTH(incomes) DO
    income ← incomes[month]
    total ← total + income
    PRINT "Month", month, "Income", income, "Total", total
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """Print report based on incomes."""
    # Note that we do not need to pass in number_of_months
    # because we know the length of the incomes list
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()