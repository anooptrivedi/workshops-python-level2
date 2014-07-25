import math

def menu():
    print("")
    print("Welcome to Geometry 101")
    print("-----------------------")

    print("For Area of a Rectangle, type 1")
    print("For Area of a Circle, type 2")
    print("For Area of a Triangle, type 3")
    print("For Area of a Trapezoid, type 4")
    print("For Area of a Parallelogram, type 5")

    print("For Volume of a Cylinder, type 6")
    print("For Volume of a Cone, type 7")
    print("For Volume of a Cube, type 8")
    print("For Volume of a Sphere, type 9")

    print("For Circumference of a Circle, type 10")

    print("To Quit, type -1")

# Area of a Rectangle is: width * height

def area_rectangle(width, height):
    return width*height

# Area of a Triangle is: PI * radius^2

def area_circle(radius):
    return math.pi*(radius**2)

# Area of a Triangle is: 1/2 * base * height

def area_triangle(base,height):
    return 0.5*base*height

# Area of a Trapezoid is: 1/2 * base1 * base2 * height

def area_trapezoid(base1,base2,height):
    return 0.5*base1*base2*height

# Area of a Parallelogram is: base * height

def area_parallelogram(base,height):
    return base*height

# Volume of a Cylinder is: PI * Height * radius^2

def volume_cylinder(radius,height):
    basearea = math.pi*(radius**2)
    return basearea*height

# Volume of a Cone is: 1/3 * PI * Height * radius^2

def volume_cone(radius,height):
    return (0.3)*math.pi*height*(radius**2)

# Volume of a Cube is: Length * Height * Width

def volume_cube(length,width,height):
    return length*height*width

# Volume of a Sphere is: 4/3 * PI * radius^3

def volume_sphere(radius):
    return (1.33)*math.pi*(radius**3)

# Circumference of a Circle is: 2 * PI * radius

def circumference_circle(radius):
    return 2*math.pi*radius

def Main():

    while True:
        menu()

        action = int(input("Choose from Option 1 to 10: "))

        if action == '-1':
            break
        elif action == 1:
            width = int(input('What is the width of the Rectangle?: '))
            height = int(input('What is the height of the Rectangle?: '))
            print("The area of Rectangle is:", area_rectangle(width, height))

        elif action == 2:
            radius = int(input('What is the radius of the Circle?: '))
            print("The area of Circle is:", round(area_circle(radius),2))

        elif action == 3:
            base = int(input('What is the base of the Triangle?: '))
            height = int(input('What is the height of the Triangle?: '))
            print("The area of Triangle is:", round(area_triangle(base,height),2))

        elif action == 4:
            base1 = int(input('What is the base 1 of the Trapezoid?: '))
            base2 = int(input('What is the base 2 of the Trapezoid?: '))
            height = int(input('What is the height of the Trapezoid?: '))
            print("The area of Trapezoid is:", round(area_trapezoid(base1,base2,height),2))

        elif action == 5:
            base = int(input('What is the base of the Parallelogram?: '))
            height = int(input('What is the height of the Parallelogram?: '))
            print("The area of Parallelogram is:", round(area_parallelogram(base,height),2))

        elif action == 6:
            radius = int(input('What is the radius of base of a Cylinder?: '))
            height = int(input('What is the height of the Cylinder?: '))
            print("The volume of Cylinder is:", round(volume_cylinder(radius,height),2))

        elif action == 7:
            radius = int(input('What is the radius of base of a Cone?: '))
            height = int(input('What is the height of the Cone?: '))
            print("The volume of Cone is:", round(volume_cone(radius,height),2))

        elif action == 8:
            length = int(input('What is the length of base of a Cube?: '))
            width = int(input('What is the width of base of a Cube?: '))
            height = int(input('What is the height of the Cube?: '))
            print("The volume of Cube is:", round(volume_cube(length,width,height),2))

        elif action == 9:
            radius = int(input('What is the radius of a Sphere?: '))
            print("The volume of Sphere is:", round(volume_sphere(radius),2))

        elif action == 10:
            radius = int(input('What is the radius of a Circle?: '))
            print("The circumference of Circle is:", round(circumference_circle(radius),2))

        else:
            action = int(input("Choose a shape to calculate area: "))


Main()




