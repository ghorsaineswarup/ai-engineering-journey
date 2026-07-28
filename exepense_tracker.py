class Expense:
    def __init__(self,amount,category,date,description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description


my_exepnse = Expense(20.0, "food" ,"2026-07-28", "lunch with family ")
print(my_exepnse.amount)
print(my_exepnse.category)
print(my_exepnse.date)
print(my_exepnse.description)     