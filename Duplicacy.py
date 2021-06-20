str = "Kriti Jain"
print("Duplicate Letter in a string:");
for i in range(0, len(str)):
    count = 1;
    for j in range(i+1, len(str)):
        if(str[i] == str[j] and str[i] != ' '):
            count = count + 1;
            string = str[:j] + '0' + str[j+1:];
    if(count > 1 and str[i] != '0'):
        print(str[i]);