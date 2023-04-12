class BankAccount:
	
    def __init__(self, int_rate): 
        self.int_rate = int_rate
        self.interest = 0
        self.balance = 0
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    
    def deposit(self, amount):
        self.balance+= amount
        return self
	
    
    def yield_interest(self):
        if self.balance > 0:
            self.interest += self.balance * self.int_rate
            self.deposit(self.interest)
        else:
            self.balance -= 5.00



class User:

    def __init__(self, name, gender, city, state, interest_rate):
        self.name = name
        self.gender = gender
        self.city = city
        self.state = state
        self.myAccount = BankAccount(interest_rate)

    def user_deposit(self, amount):
        self.myAccount.deposit(amount)
        return self

    def user_withdrawal(self, amount):
        self.myAccount.withdraw(amount)

    def display(self):
        #return BankAccount.balance
        return f"I am: {self.name}, I have {self.myAccount.balance} in my account"

    



Mela_Love = User("Mela", "Love", "Tirana", "Albania", .003)
Mela_Love.user_deposit(5000).user_withdrawal(3000)


print(Mela_Love.display())