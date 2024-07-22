from django.db import models
from django.db.utils import IntegrityError


# Create your models here.
class Account(models.Model):
    username=models.CharField(max_length=20, unique=True, default='default_username')
    account_number = models.CharField(max_length=20, )
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta: 
        unique_together=('username','account_number')

    def __str__(self):
        return f"Account {self.account_number}"

class Transaction(models.Model):
    Account = models.ForeignKey(Account, on_delete=models.CASCADE )
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.description} - ${self.amount}"

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, username, account_number, initial_balance=0):
        try:
            if not Account.objects.filter(username=username, account_number=account_number).exists():
                Account.objects.create(username=username, account_number=account_number, balance=initial_balance)
                return "Account created successfully."
            else:
                return "Account already exists for this user."
        except IntegrityError as e:
            return f"An error occurred: {str(e)}"

    def deposit(self, account_number, amount):
        try:
            account = Account.objects.get(account_number=account_number)
            account.balance =account.balance + amount
            account.save()
            return f"Deposited {amount} into account {account_number}."
        except Account.DoesNotExist:
            return "Incorrect account details."
        

    def withdraw(self, account_number, amount):
        try:
            account = Account.objects.get(account_number=account_number)
            if account.balance >= amount:
                account.balance -= amount
                account.save()
                return f"Withdraw {amount} from account {account_number}."
            else:
                return "Insufficient balance."
        except Account.DoesNotExist:
            return "Incorrect account details."

    def check_balance(self, account_number):
        try:
            account = Account.objects.get(account_number=account_number)
            return f"Your account balance is {account.balance}."
        except Account.DoesNotExist:
            return "Incorrect account details."