class Expense:
    def __init__(self, amount, category, date, description):
        if date == "":
            raise ValueError("Date cannot be empty")
        
        if amount < 0:
            raise ValueError("you cannot put negative amount")
        
        if category == "":
            raise ValueError("Your category is empty please fill up")
        
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description


class ExpenseTracker:
    def __init__(self):
        self.expenses = []   
    def add_expense(self, expense):
        self.expenses.append(expense)

    def list_expenses(self):
        for expense in self.expenses:
            print(expense.amount, expense.category, expense.date, expense.description)

    def total_spent(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total

    def total_by_category(self, category):
        total = 0
        for expense in self.expenses:
            if expense.category == category:
                total += expense.amount
        return total


tracker = ExpenseTracker()

 
expense2 = Expense(50.0, "rent", "2026-07-28", "monthly rent")
expense3 = Expense(10.0, "food", "2026-07-29", "coffee")
 
tracker.add_expense(expense2)
tracker.add_expense(expense3)

try:
    expense1=Expense(-20.0, "food", "2026-07-28", "lunch with family")
    tracker.add_expense(expense1)
except ValueError as e:
    print("Could not add expense:",e)

tracker.list_expenses()
print("Total spent:", tracker.total_spent())
print("Total on food:", tracker.total_by_category("food"))