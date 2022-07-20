# Program to make temperature convertor

# Function to convert celsius to fahrenheit
def celsius_fahrenheit():
    celsius = float(input("Enter the temperature in celsius: "))

    fahrenheit = ((celsius * 9) / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)


# Function to convert fahrenheit to celsius
def fahrenheit_celsius():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

    celsius = ((fahrenheit - 32) * 5) / 9
    print("Temperature in Celsius:", celsius)


# Function to convert kelvin to Celsius
def kelvin_celsius():
    kelvin = float(input("Enter the temperature in Kelvin: "))

    celsius = (kelvin - 273.15)
    print("Temperature in celsius:", celsius)


# Function to convert celsius to kelvin
def celsius_kelvin():
    celsius = float(input("Enter the temperature in celsius: "))

    kelvin = celsius + 273.15
    print("Temperature in Kelvin:", kelvin)


# Function to convert kelvin to fahrenheit
def kelvin_fahrenheit():
    kelvin = float(input("Enter the temperature in kelvin: "))

    fahrenheit = (((kelvin - 273.15) * 9) / 5) + 32
    print("Temperature in fahrenheit:", fahrenheit)


# Function to convert fahrenheit to kelvin
def fahrenheit_kelvin():
    fahrenheit = float(input("Enter the temperature in fahrenheit: "))

    kelvin = (((fahrenheit - 32) * 5) / 9) + 273.15
    print("Temperature in Kelvin:", kelvin)


choice = 1
while choice != 7:
    print("\n*** Temperature Convertor ***")
    print("1.   celsius to Fahrenheit")
    print("2.   Fahrenheit to celsius")
    print("3.   Kelvin to celsius")
    print("4.   celsius to Kelvin")
    print("5.   Kelvin to Fahrenheit")
    print("6.   Fahrenheit to Kelvin")
    print("7.   EXIT")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        celsius_fahrenheit()

    elif choice == 2:
        fahrenheit_celsius()

    elif choice == 3:
        kelvin_celsius()

    elif choice == 4:
        celsius_kelvin()

    elif choice == 5:
        kelvin_fahrenheit()

    elif choice == 6:
        fahrenheit_kelvin()

    elif choice == 7:
        print("Thanks For Using")

    else:
        print("!! Enter Right Choice !!")
