class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrew:", amount)
        else:
            print("Not enough money")

    def show_balance(self):
        print("Balance:", self.balance)


# Example run
acc = BankAccount("Kaium", 50)
acc.show_balance()
