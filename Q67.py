str = input("Enter any string: ")
count = 0
for i in str:
    if i.islower() == True:
        count = count + 1

print(f"There is total {count} lowercase in {str}")
