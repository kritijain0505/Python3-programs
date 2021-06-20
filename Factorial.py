#Factorial of Bigger Number
def fact(n):
    f=1
    while n:
        f=f*n
        n-=1
        return f


#Factorial using In-Buit Function
import math
n = int(input("Enter the number: "))
result=math.factorial(n)
print("Factorial of",n,"is",result)


#Factorial using Recursive Function
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter the number: "))
result=factorial(n)
print("Factorial of",n,"is",result)


#Factorial using For Loop
n=int(input("Enter a number: "))
result=1
for i in range(n,0,-1):
    result= result*i
print("Factorial of",n,"is ",result)

