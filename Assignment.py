#program to calculate Greatest Common divisor through recursion
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD=gcd(a,b)
print("GCD is: ")
print(GCD)
#%%
#Program to calculate exp(x,y) using recursive functions
def power(base,exp):
    if(exp==1):
        return(base)
    else:
        return (base*power(base,exp-1))
base=int(input("Enter the base number-"))
exp=int(input("Enter the exponential value-"))
print("Result:",power(base,exp))
#%%
#Program to print the Fibonacci series using recursion
def fibo_series(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibo_series(n-1) + fibo_series(n-2))  
 
terms = int(input("How many terms? "))  
 
if terms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(terms):  
       print(fibo_series(i))  
#%%
#Program to find the number of times a recursive function is called
def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res	

n= int(input("enter your number-"))
print(factorial(n))
#%%to concatenate two strings by recursion
#doubt

import random
def test(input_string):
    l = len(input_string)                                                   
    if l >= 10:
        return input_string
    input_string += random.choice('abcdefghijklmnopqrstuvwxyz'
                                  'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return test(input_string)                                               

input_string = ''                                                           
input_string = test(input_string)                                           
print(input_string)
#%%
#program to perform basic calculations
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number1 = int(input('Please enter the first number: '))
    number2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number1, number2))
        print(number1 + number2)

    elif operation == '-':
        print('{} - {} = '.format(number1, number2))
        print(number1 - number2)

    elif operation == '*':
        print('{} * {} = '.format(number1, number2))
        print(number1 * number2)

    elif operation == '/':
        print('{} / {} = '.format(number1, number2))
        print(number1 / number2)

    else:
        print('You have not typed a valid operator, please run the program again.')

calculate()
#%% program to calculate smallest of two numbers
small= lambda x,y:a if (a<b) else b 
num1=int(input("enter 1st number :"))
num2=int(input("enter 2nd number :"))
s=small(num1,num2)
print(s) 
#%%
#program to compute lambda(n) for all positive values of n where lambda(n) can be recursively defined as lambda(n) = lambda(n/2) +1 if n>1
func=lambda x:0 if x<=1 else func(x/2)+1  
n1=int(input("enter the starting value: "))
ans=func(n1)
print(ans)           
    
   