x=int(input("Enter the Year"))
result= "Leap Year"
if x%400==0:
    print(result)
elif x % 4 == 0 and x % 100 != 0:
    print(result)
else:
    print("non leap year")
