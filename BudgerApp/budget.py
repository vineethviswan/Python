class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
    
    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount
    
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):            
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return self.balance >= amount
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            amount = f"{entry['amount']:.2f}"
            description = entry['description'][:23]
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.balance:.2f}"
        return title + items + total

def create_spend_chart(categories):
    total_spent = sum(-entry['amount'] for category in categories for entry in category.ledger if entry['amount'] < 0)
    percentages = [(sum(-entry['amount'] for entry in category.ledger if entry['amount'] < 0) / total_spent) * 100 for category in categories]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        chart += "     "
        for category in categories:
            chart += f"{category.name[i] if i < len(category.name) else ' '}  "
        chart += "\n"

    return chart.rstrip("\n")