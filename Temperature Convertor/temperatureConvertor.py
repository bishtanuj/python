# Program to make temperature convertor

# Function to convert celcius to fahrenheit
def celcius_fahrenheit():
    celcius = float(input("Enter the temperature in celcius: "))

    fahrenheit = ((celcius * 9) / 5) + 32
    print("Temperature in Fahrenheit:",fahrenheit)

# Function to convert fahrenheit to celcius
def fahrenheit_celcius():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

    celcius = ((fahrenheit - 32) * 5) / 9
    print("Temperature in Celcius:",celcius)

# Function to convert kelvin to celcius
def kelvin_celcius():
    kelvin = float(input("Enter the temperature in Kelvin: "))

    celcius = (kelvin - 273.15)
    print("Temperature in Celcius:",celcius)

# Function to convert celcius to kelvin
def celcius_kelvin():
    celcius = float(input("Enter the temperature in celcius: "))
    
    kelvin = celcius + 273.15
    print("Temperature in Kelvin:",kelvin)

# Function to convert kelvin to fahrenheit
def kelvin_fahrenheit():
    kelvin = float(input("Enter the temperature in kelvin: "))

    fahrenheit = (((kelvin - 273.15) * 9) / 5) + 32
    print("Temperature in fahrenheit:",fahrenheit)

# Function to convert fahrenheit to kelvin
def fahrenheit_kelvin():
    fahrenheit = float(input("Enter the temperature in fahrenheit: "))

    kelvin = (((fahrenheit - 32) * 5) / 9) + 273.15
    print("Temperature in Kelvin:",kelvin)

choice = 1
while(choice != 7):
    print("\n*** Temperature Convertor ***")
    print("1.   Celcius to Fahrenheit")
    print("2.   Fahrenheit to Celcius")
    print("3.   Kelvin to Celcius")
    print("4.   Celcius to Kelvin")
    print("5.   Kelvin to Fahrenheit")
    print("6.   Fahrenheit to Kelvin")
    print("7.   EXIT")

    choice = int(input("Enter Your Choice: "))

    if(choice == 1):
        celcius_fahrenheit()
    
    elif(choice == 2):
        fahrenheit_celcius()
    
    elif(choice == 3):
        kelvin_celcius()
    
    elif(choice == 4):
        celcius_kelvin()

    elif(choice == 5):
        kelvin_fahrenheit()
    
    elif(choice == 6):
        fahrenheit_kelvin()

    elif(choice == 7):
        print("Thanks For Using")
    
    else:
        print("!! Enter Right Choice !!")
