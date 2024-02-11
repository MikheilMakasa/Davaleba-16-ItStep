class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"ანგარიშზე შეტანილი იქნა {amount} ლარი. ახალი ბალანსი: {self.balance} ლარი.")
        else:
            print("არასწორი ოპერაცია, შეიტანეთ დადებითი რიცხვი.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"ანგარიშიდან გატანილი იქნა {amount} ლარი. ახალი ბალანსი: {self.balance} ლარი.")
        else:
            print("შეტანილი რიცხვი არასწორია ან ანგარიშზე არ არის საკმარისი თანხა.")

    def show_balance(self):
        print(f"{self.account_holder}-ის ანგარიშზე არსებული ბალანსი შეადგენს: {self.balance} ლარს")



test_account1 = BankAccount("7777", "Mikheil Makasarashvili", 10000.0)
test_account2 = BankAccount("8888", "Shota Rustaveli", 20000.0)

test_account1.show_balance()
test_account1.deposit(3000.0)
test_account1.withdraw(500.0)

test_account2.show_balance()
test_account2.withdraw(1000.0)
test_account2.deposit(5000.0)
