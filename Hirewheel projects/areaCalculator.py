#intro and ask user for shape
shape = input("I can calculate the area of a shape for you. \nWhich shape do you want me to calculate the area of?")
#create list of shapes for validation
valid_shapes = ["circle", "rectangle", "square", "triangle"]
#check if shape is valid
#address invalid inputs gracefully: unexpected shape or non-numeric measurements

while shape.lower() not in valid_shapes:
    shape = input("Sorry, I can only calculate the area of a circle, rectangle, square, or triangle. Please enter one of these shapes:")

#calculate area for specific shapes and print result

if shape.lower() == "circle":
    radius = input("Please enter the radius of the circle: ")
    #address non-numeric input for radius
    while True:
        try:
            radius = float(radius)
            break
        except ValueError:
            radius = input("Invalid input. Please enter a numeric value for the radius of the circle:")
    area = 3.14159 * radius ** 2
    print(f"The area of the circle is {area:.2f}")

elif shape.lower() == "rectangle":
    length = input("Please enter the length of the rectangle: ")
    width = input("Please enter the width of the rectangle: ")
    #address non-numeric input for length and width
    while True:
        try:
            length = float(length)
            width = float(width)
            break
        except ValueError:
            length = input("Invalid input. Please enter a numeric value for the length of the rectangle:")
            width = input("Invalid input. Please enter a numeric value for the width of the rectangle:")
    area = length * width
    print(f"The area of the rectangle is {area:.2f}")

elif shape.lower() == "square":
    side = input("Please enter the side length of the square:")
    #address non-numeric input for side length
    while True:
        try:
            side = float(side)
            break
        except ValueError:
            side = input("Invalid input. Please enter a numeric value for the side length of the square:")
    area = side ** 2
    print(f"The area of the square is {area:.2f}")

elif shape.lower() == "triangle":
    base = input("Please enter the base length of the triangle:")
    height = input("Please enter the height of the triangle:")
    #address non-numeric input for base and height
    while True:
        try:
            base = float(base)
            height = float(height)
            break
        except ValueError:
            base = input("Invalid input. Please enter a numeric value for the base length of the triangle:")
            height = input("Invalid input. Please enter a numeric value for the height of the triangle:")
    area = 0.5 * base * height
    print(f"The area of the triangle is {area:.2f}")
