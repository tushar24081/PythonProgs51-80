n = int(input("Enter Number: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print("*", end="")
    print()
for i in range(1, n+1):
    for k in range(n-1, i-1, -1):
        print("*", end="")
    print()
