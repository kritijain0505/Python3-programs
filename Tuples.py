#Sort  a List of numbers
l=[int(e) for e in input("Enter numbers separated by comma").split(',')]
print(l)
l.sort()
print(l)



#reverse a tuple
t=eval(input("Enter numbers separated by comma"))
print("User entered Tuple is",t)
l=list(t)
l.reverse()
t=tuple(l)
print("Reverse of Tuple is : ",t)





#To count the frequency of elements of a tuple
print("Enter numbers separated by comma")
t1=tuple([int(e) for e in input().split(',')])
i=0
for e in t1:
    if i==t1.index(e):
        print(e,' - ',t1.count(e))
    i+=1



#To merge two sorted tuple
t1=(10,20,30,40)
t2=(5,9,12,18,22,25)
t3=[]
i,j,k=0,0,0
while i<len(t1) and j<len(t2):
    if t1[i]<t2[j]:
        t3.append(t1[i])
        i+=1
        k+=1
    else:
        t3.append(t2[j])
        j+=1
        k+=1
if i==len(t1):
    while j<len(t2):
        t3.append(t2[j])
        j+=1
        k+=1
elif j==len(t2):
    while i<len(t1):
        t3.append(t1[i])
        i+=1
        k+=1
t3=tuple(t3)
print("Resulting Tuple is : ",t3)


#To Compare Two Tuple
print("Enter elements separated by comma for first tuple ")
t1=tuple([eval(e) for e in input().split(',')])
print("Enter elements separated by comma for Second tuple ")
t2=tuple([eval(e) for e in input().split(',')])
if t1==t2:
    print("Yes, Tuples are same")
else:
    print("No, Tuples are not same")



#To Find Greatest Number From a Tuple Of int values
print("Enter numbers separated by commas")
t1=tuple([int(e) for e in input().split(',')])
print("Greatest numbers in the tuple is", max(t1))
