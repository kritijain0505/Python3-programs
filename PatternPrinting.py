#Pattern 1
for i in range(1,5):                             #Row
    for j in range(1,5):                         #column
        if  j>=i:
            print("*",end='')
        else:
            print(" ",end='')
    print()



#pattern 2
n=int(input("Enter the number of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()



#pattern 3
n=int(input("Enter the number of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()



#pattern 4
n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        if j==0 or i==(n-1) or i==j:
            print("*",end="")
        else:
            print(end=" ")
    print()


#Pattern 5
n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == (n - 1) or i == j:
            print("*", end="")
        else:
            print(end=" ")
    print()


#Pattern 6 Floyd's Triangle
n=int(input("Enter the number of rows: "))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()


#Pattern 7   Strings in the Right Triangle Shape
String = input("Enter the String")
length= len(String)
for i in range(length):
    for j in range(i+1):
        print(String[j],end="")
    print()


#Pattern 8   Numbers in the Right Triangle Shape
n=int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()



#Pattern 8   Numbers in the Right Triangle Shape
n=int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print()

#pattern 8  stars in Hollow equilateral Triangle Shape
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,2*n):
        if i==n or i+j==n+1 or j-i==n-1:
            print("*",end="")
        else:
            print(end=" ")
    print()



#pattern 9  stars in Hollow equilateral Triangle Shape
n=int(input("Enter the number of rows: "))
k=2
for i in range(1,n+1):
    for j in range(1,2*n):
        if i+j==n+1 or j-i==n-1:
            print("*",end="")
        elif i==n and j!=l:
            print("*",end="")
            k+=2
        else:
            print(end=" ")
    print()



#Pattern 10 Using While Loop
num=int(input("Enter the number of rows"))
row=0
while row<num:
    star=row+1
    while star>0:
        print("*",end="")
        star=star-1


#Pattern 11 Pyramid Shape Using While Loop
num=int(input("Enter the number of rows"))
i=0
while i<num:
    space = num-i-1
    while space>0:
        print(end=" ")
        space-=1
    star = i+1
    while star>0:
        print("*",end=" ")
        star = star-1
    i=i+1
    print()



#pattern 12 Stars in Hollow Diamond Shape
for i in range(5):
    for j in range(5):
        if i+j==2 or j-i==2 or i-j==2 or i+j==6:
            print("*",end="")
        else:
            print(end=" ")
    print()



#Pattern 13 Numbers in square shape
num=int(input("Enter the number of rows: "))
n_list=[[0 for  x in range(num)] for y in range(num)]
low=0
high=num-1
count=int((num+1)/2)
for i in range(count):
    for j in range(low,high+1):
        n_list[i][j]=n
        n=n+1
    for j in range(low+1,high+1):
        n_list[j][high]=n
        n=n+1
    for j in range(high-1,low-1,-1):
        n_list[high][j]=n
        n=n+1
    for j in range(high-1,low-1):
        n_list[j][]=n
        n=n+1
    low=low+1
    high=high-1
for i in range(num):
    for j in range(num):
        print(n_list[i][j],end="\t")
    print()


#Pattern 14 Numbers in pyramid shape
num = int(input("Enter the number of rows: "))
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(end="")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()
    