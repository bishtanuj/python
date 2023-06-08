# Program to make temperature convertor

# Function to convert Celsius to Fahrenheit
def celsius_fahrenheit():
    celsius = float(input("Enter the temperature in celsius: "))

    fahrenheit = ((celsius * 9) / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)


# Function to convert Fahrenheit to Celsius
def fahrenheit_celsius():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

    celsius = ((fahrenheit - 32) * 5) / 9
    print("Temperature in Celsius:", celsius)


# Function to convert kelvin to Celsius
def kelvin_celsius():
    kelvin = float(input("Enter the temperature in Kelvin: "))

    celsius = (kelvin - 273.15)
    print("Temperature in celsius:", celsius)


# Function to convert Celsius to kelvin
def celsius_kelvin():
    celsius = float(input("Enter the temperature in celsius: "))

    kelvin = celsius + 273.15
    print("Temperature in Kelvin:", kelvin)


# Function to convert kelvin to Fahrenheit
def kelvin_fahrenheit():
    kelvin = float(input("Enter the temperature in kelvin: "))

    fahrenheit = (((kelvin - 273.15) * 9) / 5) + 32
    print("Temperature in fahrenheit:", fahrenheit)


# Function to convert Fahrenheit to kelvin
def fahrenheit_kelvin():
    fahrenheit = float(input("Enter the temperature in fahrenheit: "))

    kelvin = (((fahrenheit - 32) * 5) / 9) + 273.15
    print("Temperature in Kelvin:", kelvin)


if __name__ == "__main__":
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

        match choice:
            case 1:
                celsius_fahrenheit()
            case 2:
                fahrenheit_celsius()
            case 3:
                kelvin_celsius()
            case 4:
                celsius_kelvin()
            case 5:
                kelvin_fahrenheit()
            case 6:
                fahrenheit_kelvin()
            case 7:
                print("Thanks For Using")
            case _:
                print("!! Enter Right Choice")
