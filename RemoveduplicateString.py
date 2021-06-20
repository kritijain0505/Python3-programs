name = []
n = int(input("Enter the number of names you want to enter"))
for i in range(n):
    print(i+1,'enter names')
    name.append(input())
s = set(name)
name = list(s)
for x in name:
    print(x)


#to remove duplicate characters fron a string
s= input("Enter a string")
i=0
s1=""
for x in s:
    if s.index(x)==i:
        s1+=x
    i+=1
print(s1)

#Reverse a String
s=input("Enter a string")
print(s[len(s)-1::-1])          #slicing operator



#Reverse a String
def reverse(string):
    reversed_string= ""
    for i in string:
        reversed_string = i+reversed_string
    print("Reversed string is: ",reversed_string)
string = input("Enter a string: ")
print("Entered string: ", string)
reverse(string)