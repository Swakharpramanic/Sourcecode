rows = int(input("Please enter how many rows you need: "))  
for i in range(rows, 0, -1):  
    for j in range(1, i + 1):  
        print(j, end=' ')  
    print () #for printing a new line  
