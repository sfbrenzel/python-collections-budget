from . import Expense

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
for expense in expenses.list:
    expense.amount.append(myBudgetList)

class BudgetList():
    """docstring forBudgetList."""

    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def append(self, item):
            if (self.sum_expenses + item < self.budget):
                self.expenses.append(item)
                self.sum.expenses + item
            else
                self.overages.append(item)
                self.sum.overages + item

    def __len__(self):
        return (self.expenses + self.sum_overages)

def main():
    myBudgetList = BudgetList(1200)

    print('the count of all expenses:' + str(len(myBudgetList)))

    if __name__ == "__main__"
        main()
