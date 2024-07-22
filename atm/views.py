from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import Bank ,Account,Transaction
from django.http import HttpResponse
from decimal import Decimal

# Create your views here.

def home(request):

    return render (request,'home.html')

def register(request): 
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password']
        email=request.POST['email']
        if password ==password1 :
            if User.objects.filter(email=email).exists():
                messages.error(request,'your email already exist')
                return redirect('login')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save()
                messages.success(request, 'Your account has been created successfully.')
                return redirect('login')     
        else:
            messages.error(request,"password not match")
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST': 
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None: 
            auth_login(request,user)
            messages.success(request, f'You are now logged in as {username}.')
            return redirect('dashboard')
        else:
            messages.error(request,'your credential is wrong')
            return redirect('login')

    return render (request ,'login.html')

def forgot_password(request): 
    return render(request ,'forgot_password.html')

def dashboard(request): 
    return render(request,'dashboard.html')



bank=Bank('ravi')

def create(request): 
    message = ""
    if request.method=='POST':
        username=request.POST['username']
        account_number=request.POST['account_number']
        initial_balance = float(request.POST.get('initial_balance', 0))
        message=bank.create_account(username,account_number,initial_balance)
    return render(request,'create_account.html', {'message': message})

def withdrawal(request):
    message=""
    if request.method=='POST': 
        account_number=request.POST['account_number']
        amount=float(request.POST['amount'])
        amount=Decimal(amount)
        message=(bank.withdraw(account_number,amount))
        Transaction.objects.create(
            Account=Account.objects.get(account_number=account_number), 
            description='withdraw',
            amount=amount
        )
        messages.success(request,message)
        return redirect('withdraw')
    return render (request,'withdrawal.html')

def deposit(request):
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        amount = float(request.POST.get('amount', 0))  
        amount = Decimal(amount)  
        message = bank.deposit(account_number, amount)
        
        # Create a transaction record
        Transaction.objects.create(
            Account=Account.objects.get(account_number=account_number), 
            description='Deposit',
            amount=amount
        )
        
        messages.success(request, message)
        
        return redirect('deposit')
    
    return render(request, 'deposit.html')

def check_balance(request): 
    message=""
    if request.method=='POST': 
        account_number=request.POST['account_number']
        message=(bank.check_balance(account_number))
        messages.error(request,message)
        return redirect('check_balance')
    return render (request,'check_balance.html')


def mini_statement(request):
   
    account_number = 'user_account_number' 
   
    transactions = Transaction.objects.filter(Account__account_number=account_number).order_by('-date')[:10]

    return render(request, 'mini_statement.html', {'transactions': transactions})
