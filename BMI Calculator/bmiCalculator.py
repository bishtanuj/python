# Program to calculate BMI

# Scanning the height from the user
height = float(input("Enter your height in metre: "))

# Scanning the weight from the user
weight = float(input("Enter your weight in kilogram: "))

# Calculating BMI
BMI = weight / height ** 2

# Printing the BMI
print("\nYour BMI: ", BMI)

# Printing the conclusion
if(BMI < 18.5):
    print("Conclusion:  UNDERWEIGHT")
elif(BMI > 18.5 and BMI < 24.9):
    print("Conclusion: HEALTHY")
elif(BMI > 25.0 and BMI < 29.9):
    print("Conclusion:  OVERWEIGHT")
else:
    print("Conclusion:  OBESE")
