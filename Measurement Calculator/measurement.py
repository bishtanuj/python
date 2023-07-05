# Program to compute measurements

from math import pi


# Function to compute perimeter of circle
def perimeterOfCircle():
    radius = float(input("Enter the radius of circle: "))

    perimeter = 2 * pi * radius
    print("Perimeter of Circle: ", perimeter)


# Function to compute perimeter of Rectangle
def perimeterOfRectangle():
    length = float(input("Enter the length of rectangle: "))
    breadth = float(input("Enter the breadth of rectangle: "))

    perimeter = 2 * length + breadth
    print("Perimeter of Rectangle:", perimeter)


# Function to compute perimeter of Rhombus
def perimeterOfRhombus():
    side = float(input("Enter the length of one side of Rhombus: "))

    perimeter = 4 * side
    print("Perimeter of Rhombus: ", perimeter)


# Function to compute perimeter of Square
def perimeterOfSquare():
    side = float(input("Enter the length of one side of Square: "))

    perimeter = 4 * side
    print("Perimeter of Square:", perimeter)


# Function to compute perimeter of Triangle
def perimeterOfTriangle():
    side_1 = float(input("Enter the length of side I: "))
    side_2 = float(input("Enter the length of side II: "))
    side_3 = float(input("Enter the length of side III: "))

    perimeter = side_1 + side_2 + side_3
    print("Perimeter of Triangle: ", perimeter)


# Function to compute the area of Circle
def areaOfCircle():
    radius = float(input("Enter the radius of circle: "))

    area = pi * radius ** 2
    print("Area of Circle: ", area)


# Function to compute the area of Rectangle
def areaOfRectangle():
    length = float(input("Enter the length of Rectangle: "))
    breadth = float(input("Enter the breadth of Rectangle: "))

    area = length * breadth
    print("Area of Rectangle: ", area)


# Function to compute the area of Rhombus
def areaOfRhombus():
    diagonalone = float(input("Enter the length of the diagonal I: "))
    diagonaltwo = float(input("Enter the length of the diagonal II: "))

    area = (diagonalone * diagonaltwo) / 2
    print("Area of Rhombus: ", area)


# Function to compute the area of Square
def areaOfSquare():
    side = float(input("Enter the length of one side of Square: "))

    area = side * side
    print("Area of Square: ", area)


# Function to compute the area of Triangle
def areaOfTriangle():
    height = float(input("Enter the height of the Triangle: "))
    base = float(input("Enter the length of the base of the Triangle: "))

    area = (height * base) / 2
    print("Area of Triangle: ", area)


# Function to compute the volume of Cylinder
def volumeOfCylinder():
    radius = float(input("Enter the radius of the Cylinder: "))
    height = float(input("Enter the height of the Cylinder: "))

    volume = pi * height * radius ** 2
    print("Volume of Cylinder: ", volume)


# Function to compute the volume of Cuboid
def volumeOfCuboid():
    length = float(input("Enter the length of the Cuboid: "))
    breadth = float(input("Enter the breadth of the Cuboid: "))
    height = float(input("Enter the height of the Cuboid: "))

    volume = length * breadth * height
    print("Volume of Cuboid: ", volume)


# Function to compute the volume of Cube
def volumeOfCube():
    edge = float(input("Enter the length of one edge of Cube: "))

    volume = edge ** 3
    print("Volume of Cube: ", volume)


# Function to compute the volume of the Cone
def volumeOfCone():
    radius = float(input("Enter the radius of the Cone: "))
    height = float(input("Enter the height of the Cone: "))

    volume = (pi * height * radius ** 2) / 3
    print("Volume of Cone: ", volume)


# Function to compute the volume of the Sphere
def volumeOfSphere():
    radius = float(input("Enter the radius of the Sphere: "))

    volume = (4 * pi * radius ** 3) / 3
    print("Volume of Sphere: ", volume)


# Function to compute the volume of the Hemisphere
def volumeOfHemisphere():
    radius = float(input("Enter the radius of the Hemisphere: "))

    volume = (2 * pi * radius ** 3) / 3
    print("Volume of Hemisphere: ", volume)


print("\n*** OPERATIONS ***")
print("1. Compute Perimeter")
print("2. Compute Area")
print("3. Compute Volume")

choice = int(input("Enter your choice: "))
match choice:
    # To compute Perimeter
    case 1:
        print("*** Select Shape ***")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Rhombus")
        print("4. Square")
        print("5. Triangle")
    
        choice_1 = int(input("Enter your choice: "))
        match choice_1:
            case 1:
                perimeterOfCircle()
            case 2:
                perimeterOfRectangle()
            case 3:
                perimeterOfRhombus()
            case 4:
                perimeterOfSquare()
            case 5:
                perimeterOfTriangle()
            case _:
                print("!! Enter Right Choice !!")
    
    # To compute Area
    case 2:
        print("*** Select Shape ***")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Rhombus")
        print("4. Square")
        print("5. Triangle")
    
        choice_2 = int(input("Enter your choice: "))
        match choice_2:
            case 1:
                areaOfCircle()
            case 2:
                areaOfRectangle()
            case 3:
                areaOfRhombus() 
            case 4:
                areaOfSquare()
            case 5:
                areaOfTriangle()
            case _:
                print("!! Enter Right Choice !!")

    # To compute Volume
    case 3:
        print("*** Select Shape ***")
        print("1. Cylinder")
        print("2. Cuboid")
        print("3. Cube")
        print("4. Cone")
        print("5. Sphere")
        print("6. Hemisphere")
    
        choice_3 = int(input("Enter your choice: "))
    
        if choice_3 == 1:
            volumeOfCylinder()
    
        elif choice_3 == 2:
            volumeOfCuboid()
    
        elif choice_3 == 3:
            volumeOfCube()
    
        elif choice_3 == 4:
            volumeOfCone()
    
        elif choice_3 == 5:
            volumeOfSphere()
    
        elif choice_3 == 6:
            volumeOfHemisphere()
    
        else:
            print("!! Enter Right Choice !!")
    
    else:
        print("!! Enter Right Choice !!")
