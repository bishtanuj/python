# Program to print the table

# scanning the number
num = int(input("Enter a number: "))

# printing the table
print(f"Table of {num}:")
tables = [lambda x=x: x*num for x in range(1, 11)]
i = 0
for table in tables:
    i += 1
    print(f"{num} * {i} = {table()}")

    
# OUTPUT
# Enter a number: 6
# Table of 6:
# 6 * 1 = 6
# 6 * 2 = 12
# 6 * 3 = 18
# 6 * 4 = 24
# 6 * 5 = 30
# 6 * 6 = 36
# 6 * 7 = 42
# 6 * 8 = 48
# 6 * 9 = 54
# 6 * 10 = 60
