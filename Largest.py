number = []
print("enter 8 number : ")
for i in range(8):
    number.append(int(input()))
largest = number[0]
for i in range(8):
    if largest < number[i]:
        largest = number[i]

secondLargest = number[0]
for i in range(8):
    if secondLargest < number[i]:
        if number[i] != largest:
            secondLargest = number[i]

print("\n Second Largest Number is: ", end=" ")
print(secondLargest)