# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income,
# total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes 
# and its description. The same goes for expenses.

class PersonAccount:

    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def total_income(self):
        pass
    def total_expense(self):
        pass
    def account_info(self):
        pass
    def add_income(self, description, amount):
        self.incomes.append({
            'description': description,
            'amount': amount
        })
    def add_expense(self, description, amount):
        self.expenses.append({
            'description': description,
            'amount': amount
        })
    def account_balance(self):
        pass

p1 = PersonAccount('Jan', 'Sistonen', {}, {})

print(p1)
print(p1.firstname)

p1.add_income('tutoring', 100)
p1.add_expense('Car insurance', 80)
p1.add_income('Volunteer work', 80)
print(p1.expenses, ' and incomes: ', p1.incomes)