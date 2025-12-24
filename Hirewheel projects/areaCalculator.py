#intro and ask user for shape
shape = input("I can calculate the area of a shape for you. Which shape do you want me to calculate the area of?")
#create list of shapes for validation
valid_shapes = ["circle", "rectangle", "square", "triangle"]
#check if shape is valid
if shape.lower() == "circle":
    radius = float(input("Please enter the radius of the circle: "))
    area = 3.14159 * radius ** 2
    print(f"The area of the circle is {area:.2f}")
elif shape.lower() == "rectangle":
    length = float(input("Please enter the length of the rectangle: "))
    width = float(input("Please enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is {area:.2f}")
