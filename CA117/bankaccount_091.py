class BankAccount(object):
	next_account_number = 16555232
	account_type = "General"

	def __init__(self, forename, surname, balance = 0.00):
		self.forename = forename
		self.surname = surname
		self.balance = balance
		self.account_number = BankAccount.next_account_number
		self.account_type = BankAccount.account_type
		BankAccount.next_account_number += 1

	def lodge(self, other):
		self.balance = self.balance + other
		return self.balance

	def withdraw(self,other):
		if self.balance < other:
			print ("Insufficient funds available")
		else:
			self.balance = self.balance - other
			return self.balance

	def __str__(self):
		l = []
		l.append("Name: {} {}".format(self.forename, self.surname))
		l.append("Account number: {}".format(self.account_number))
		l.append("Account type: {}".format(self.account_type))
		l.append("Balance: {:.2f}".format(self.balance))
		return ("\n".join(l))

class CurrentAccount(BankAccount):
	account_type = "Current"
	def __init__(self, forename, surname,balance = 0.00):
		super().__init__(forename, surname, balance = 0.00)
		self.account_type = CurrentAccount.account_type
		self.balance = balance


	def withdraw(self, other):
		if self.balance - other > -1000:
			self.balance = self.balance - other
		else:
			print("Insufficient funds available")
		return self.balance

	def __str__(self):
		l = []
		l.append(super().__str__())
		l.append("Overdraft: {:.2f}".format(-1000))
		return "\n".join(l)

class SavingsAccount(BankAccount):
	account_type = "Savings"
	def __init__(self, forename, surname, balance = 0.00):
		super().__init__(forename, surname, balance = 0.00)
		self.account_type = SavingsAccount.account_type
		self.balance = balance

	def apply_interest(self):
		self.balance = self.balance + (self.balance * 0.01)
		return self.balance

	def __str__(self):
		l = []
		l.append(super().__str__())
		l.append("Interest rate: {}".format(0.01))
		return "\n".join(l)