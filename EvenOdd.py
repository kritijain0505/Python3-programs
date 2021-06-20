#EvenOdd Check
x=int(input('Enter a number'))
if x%2==0:
    print(x,"is even")
else:
    print(x,'id Odd')


#print table of user's choice
n=int(input("Enter a number"))
for i in range(1,11):
    print(n,"X",i,"=",n*i)
    #print("%d X %d = %d" %(n,i,n*i))    ~Formated String



#number is +ve, -ve,zero
x=int(input("Enter a number"))
if x>0:
    print("Positive")
elif x<0:
    print("Negative")
else:
    print("Zero")

#To print First 10 Odd Natural Number
i=1
while i<=19:
    print(i,end=' ')
    i+=2


#To print First N Even Natural Number in reverse order
n=int(input("Enter a natural number"))
for i in range(2*n,1,-2):
    print(i,end=' ')



#Rrcursive Function to print First N Even Natural Number in reverse order
def printEvenReverse(n):
    if n>0:
        print(2*n,end=' ')
        printEvenReverse(n-1)



#Recursive Function to print First N Even Natural Number
def printNEven(n):
    if n>0:
        printNEven(n-1)
        print(2*n,end=' ')



#To print First 10 Even Natural Number
for i in range(2,21):
    print(i,end=' ') if i%2==0 else print(end=' ')