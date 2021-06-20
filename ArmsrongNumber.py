#Armstrong Number
for i in range(1001):
    num=i
    result=0
    n=len(str(i))
    while(i!=0):
        digit=i%10
        result=result+digit**n
        i=i//10
    if num==result:
        print(num)


#Fibonacci Series
n=int(input("Enter how many numbers you want in this series: "))
first = 0
second = 1
for i in range(n):
    print(first)
    temp = first
    first = second
    second = temp + second

#Swapping two numbers using third variable
a=int(input("Enter the value for a: "))
b=int(input("Enter the value for b: "))
temp = a
a = b
b = temp
print("After Swapping: ")
print("value of a: ",a)
print("value of b: ",b)


#Swapping two numbers without using third variable
a=int(input("Enter the value for a: "))
b=int(input("Enter the value for b: "))
a=a+b
b=a-b
a=a-b
print("After Swapping: ")
print("value of a: ",a)
print("value of b: ",b)

#GCD of Two numbers
def ComputeGCD(a,b):
    if b==0:
        return a
    else:
        return ComputeGCD(b,a%b)
num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
print(ComputeGCD(num1,num2))
