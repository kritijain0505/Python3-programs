#print First 10 Natural Number
n=int(input("Enter a Number"))
for i in range(1,n+1):
    print(i,end=' ')


#reverse first 10 natural number
i=10
while i>=1:
    print(i , end=' ')
    i-=1




#Index of all occurrence of given element in a given list
l=[eval (x) for x in input("Enter list elements").split(',')]
element=eval(input("Enter element value"))
index=0
while index<len(l):
    if l[index]==element:
        print(index,end=' ')
    index+=1


#To check prime Number
n=int(input("Enter a number"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Not Prime")
            break
    else:
        print("Number is Prime")



#Prime Numbers in given interval
lower= int(input("Enter the lower interval: "))
upper= int(input("Enter the upper interval: "))
for num in range(lower,upper+1):
    if num>1:
        for j in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)


#To return next Prime Number
def nextPrime(num):
    while True:
        num+=1
        for i in range(2,num):
            if num%i==0:
                break
            else:
                return num
def PrimeProducer(N):
    num,count=1,1
    while count<=N:
        num=nextPrime(num)
        yield num
        count+=1
N =int(input("how many prime numbers you want to generate?"))
l=[x for x in PrimeProducer(N)]
print(l)


# number divisibility by 5
x=int(input("Enter a number"))
if x%5==0:
    print("%d is divisible by 5"%x)
else:
    print("%d is  not divisible by 5"%x)