#Sum of two numbers
x = int(input(" Enter the first Number "))
y = int(input(" Enter the Second Number "))
sum = x + y
print("sum of " ,x, "and" ,y, "is" ,sum,)

#Single line function-lambda to calculate factorial
f=lambda n: n*f(n-1) if n>0 else 1
print(f)

#Recursive Function to calculate sum of squares of First N natural nos.
sum=lambda n: 1 if n==1 else n**2+sum(n-1)


#Recursive Function to calculate sum of First N natural Numbers
def sumN(n):
    if n==1:
        return 1
    return  sumN(n-1)+n



#Perfect Number or not
num=int(input("Enter the number : "))
result=0
for i in range(1,num):
    if (num%i)==0:
        result=result+i
if result==num:
    print(num,"is Perfect number")
else:
    print(num,"is not perfect number")



#Perfect Number in a Given interval
lower=int(input("Enter the lower limit : "))
upper=int(input("Enter the upper limit : "))
for num in range(lower,upper+1):
    for i in range(1,num):
        if (num%i)==0:
            result=result+i
    if result == num:
        print(num)
