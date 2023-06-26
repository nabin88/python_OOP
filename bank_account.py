# This program creates a bank account and update it when the account holder draws or deposits money.

from datetime import datetime as dt 
now = dt.now()

day = now.strftime("%A, %m, %-Y")
time = now.strftime("%H:%M:%S")

class BankAccount():

	def __init__(self, name, balance):
		self.name = name
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		print(f'You deposited ${amount} on {day} at {time}.')

	def withdraw(self, amount):
		# check if the entered amount is valid
		if amount < 0:
			print('Please enter a valid amount.')
		# reject if the withdrawing amount is more than balance  
		elif self.balance < amount:
			print("Sorry! You do not have enough balance.")
		# subtract the withdrawn amount from the balance
		else:
			self.balance -= amount
			print(f'You are withdrawing ${amount} on {day} at {time}.')
	
	def checkbalance(self):
		print(f'Your account balance is ${self.balance}.')


# let's check if it works:
myacc = BankAccount('Albert', 200)

myacc.deposit(50)
myacc.withdraw(75)
myacc.checkbalance()