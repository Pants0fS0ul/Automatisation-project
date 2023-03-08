import math

# Request from the user to enter a body name and its parameters
figure = input("Enter a body name: ")
para = input("Enter the desired parameter: ")

# Calculation of the parameters desired by the user depending on the data entered
if figure == "Sphere":
    if para == "Volume":
        side = float(input("Enter the radius of the sphere: "))
        volume = 4/3 * math.pi * side ** 3
        print(f"{figure}  {volume}")
    elif para == "Surface area":
        side = float(input("Enter the radius of the sphere: "))
        area = 4 * math.pi * side ** 2
        print(f"{figure}  {area}")
    else:
        print("Mistake")

elif figure == "Cube":
    if para == "Volume":
        side = float(input("Enter the side of the cube: "))
        volume = side ** 3
        print(f"{figure} {para} is {volume}")
    elif para == "Surface area":
        side = float(input("Enter the side of the cube: "))
        area = side ** 2 * 6
        print(f"{figure} {para} is {area}")
    elif para == "Side diagonal":
        side = float(input("Enter the side of the cube: "))
        side_diagonal = side * math.sqrt(2)
        print(f"{figure} {para} is {side_diagonal}")
    elif para == "Whole cube diagonal":
        side = float(input("Enter the side of the cube: "))
        diagonal_с = math.sqrt((side * math.sqrt(2)) ** 2 + side ** 2)
        print(f"{figure} {para} is {diagonal_с}")
    else:
        print("Mistake available")

elif figure == "Parallelepiped":
    if para == "Volume":
        side_1 = float(input("Enter the length at the base of the parallelepiped: "))
        side_2 = float(input("Enter the width at the base of the parallelepiped: "))
        height = float(input("Enter the height at the base of the parallelepiped: "))
        volume = side_1 * side_2 * height
        print(f"{figure} {para} is {volume}")
    elif para == "Surface area":
        side_1 = float(input("Enter the length at the base of the parallelepiped: "))
        side_2 = float(input("Enter the width at the base of the parallelepiped: "))
        height = float(input("Enter the height at the base of the parallelepiped: "))
        area = 2 * (side_1 * side_2 + height * side_2 + side_1 * height)
        print(f"{figure} {para} is {area}")
    elif para == "Base area":
        side_1 = float(input("Enter the length at the base of the parallelepiped: "))
        side_2 = float(input("Enter the width at the base of the parallelepiped: "))
        base_area = math.sqrt(side_1 ** 2 + side_2 ** 2)
        print(f"{figure} {para} is {base_area}")
    elif para == "Smaller side by length area":
        side_2 = float(input("Enter the width at the base of the parallelepiped: "))
        height = float(input("Enter the height at the base of the parallelepiped: "))
        side_area_1 = math.sqrt(side_2 ** 2 + height ** 2)
        print(f"{figure} {para} is {side_area_1}")
    elif para == "Bigger side by length area":
        side_1 = float(input("Enter the length at the base of the parallelepiped: "))
        height = float(input("Enter the height at the base of the parallelepiped: "))
        side_area_2 = math.sqrt(side_1 ** 2 + height ** 2)
        print(f"{figure} {para} is {side_area_2}")
    elif para == "Base diagonal":
        side_1 = float(input("Enter the length at the base of the parallelepiped: "))
        side_2 = float(input("Enter the width at the base of the parallelepiped: "))
        base_diagonal = math.sqrt(side_1 ** 2 + side_2 ** 2)
        print(f"{figure} {para} is {base_diagonal}")
    elif para == "Smaller side by length side diagonal":
        side_2 = float(input("Enter the width at the base of the parallelepiped: "))
        height = float(input("Enter the height at the base of the parallelepiped: "))
        side_diagonal_1 = math.sqrt((side_2 ** 2 + height ** 2))
        print(f"{figure} {para} is {side_diagonal_1}")
    elif para == "Bigger side by length side diagonal":
        side_1 = float(input("Enter the length at the base of the parallelepiped: "))
        height = float(input("Enter the height at the base of the parallelepiped: "))
        side_diagonal_2 = math.sqrt((side_1 ** 2 + height ** 2))
        print(f"{figure} {para} is {side_diagonal_2}")
    elif para == "Whole parallelepiped diagonal":
        side_1 = float(input("Enter the length at the base of the parallelepiped: "))
        side_2 = float(input("Enter the width at the base of the parallelepiped: "))
        height = float(input("Enter the height at the base of the parallelepiped: "))
        side_diagonal_2 = math.sqrt(math.sqrt(side_1 ** 2 + side_2 ** 2) + height ** 2)
        print(f"{figure} {para} is {side_diagonal_2}")
    else:
        print("You had mistaken")

elif figure == "Cylinder":
    if para == "Volume":
        radius = float(input("Enter the radius of the circle at the base: "))
        height = float(input("Enter the cylinder height: "))
        volume = math.pi * radius ** 2 * height
        print(f"{figure} {para} is {volume}")
    elif para == "Side area":
        radius = float(input("Enter the radius of the circle at the base: "))
        height = float(input("Enter the cylinder height: "))
        side_area = 2 * math.pi * radius * height
        print(f"{figure} {para} is {side_area}")
    elif para == "Area":
        radius = float(input("Enter the radius of the circle at the base: "))
        height = float(input("Enter the cylinder height: "))
        area = 2 * math.pi * radius ** 2 + 2 * math.pi * radius * height
        print(f"{figure} {para} is {area}")
    elif para == "Base area":
        radius = float(input("Enter the radius of the circle at the base: "))
        base_area = math.pi * radius ** 2
        print(f"{figure} {para} is {base_area}")
    else:
        print("Mistake is your lifestyle")
        
elif figure == "Pyramid":
    if para == "Volume":
        side = float(input("Enter the length at the base of the pyramid: "))
        height = float(input("Enter the width at the base of the parallelepiped: "))
        volume = 1/3 * height * side ** 2
        print(f"{figure} {para} is {volume}")
    if para == "Side area":
        side = float(input("Enter the length at the base of the pyramid: "))
        height = float(input("Enter the width at the base of the parallelepiped: "))
        side_area = 1/2 * side * math.sqrt((1/2 * side) ** 2 + height ** 2) * 4
        print(f"{figure} {para} is {side_area}")
    if para == "Area":
        side = float(input("Enter the length at the base of the pyramid: "))
        height = float(input("Enter the width at the base of the parallelepiped: "))
        area = 1/2 * side * math.sqrt((1/2 * side) ** 2 + height ** 2) * 4 + side ** 2
        print(f"{figure} {para} is {area}")
    if para == "Base area":
        side = float(input("Enter the length at the base of the pyramid: "))
        base_area = side ** 2
        print(f"{figure} {para} is {base_area}")
    if para == "Rib length":
        side = float(input("Enter the length at the base of the pyramid: "))
        height = float(input("Enter the width at the base of the parallelepiped: "))
        side_area_side = math.sqrt((1/2 * side * math.sqrt(2)) ** 2 + height ** 2)
        print(f"{figure} {para} is {side_area_side}")
    if para == "Apothema":
        side = float(input("Enter the length at the base of the pyramid: "))
        height = float(input("Enter the width at the base of the parallelepiped: "))
        apothegm = math.sqrt((1/2 * side) ** 2 + height ** 2)
        print(f"{figure} {para} is {apothegm}")
    if para == "Double - plane angle":
        side = float(input("Enter the length at the base of the pyramid: "))
        height = float(input("Enter the width at the base of the parallelepiped: "))
        side_n_base_angle = height / (1/2 * side)
        print(f"{figure} {para} is {side_n_base_angle}")
    if para == "Between rib and base angle":
        side = float(input("Enter the length at the base of the pyramid: "))
        side_area_side_n_base_angle = height / (1/2 * side * math.sqrt(2))
        print(f"{figure} {para} is {side_area_side_n_base_angle}")
    else:
        print("Daun")

elif figure == "Cone":
    if para == "Volume":
        radius = float(input("Enter the radius at the base of the cone: "))
        height = float(input("Enter height: "))
        volume = 1/3 * height * math.pi * radius ** 2
        print(f"{figure} {para} is {volume}")
    if para == "Side area":
        radius = float(input("Enter the radius at the base of the cone: "))
        height = float(input("Enter height: "))
        side_area = radius * math.pi * math.sqrt(radius ** 2 + height ** 2)
        print(f"{figure} {para} is {side_area}")
    if para == "Area":
        radius = float(input("Enter the radius at the base of the cone: "))
        height = float(input("Enter height: "))
        area = radius * math.pi * math.sqrt(radius ** 2 + height ** 2) + math.pi * radius ** 2
        print(f"{figure} {para} is {area}")
    if para == "Base area":
        radius = float(input("Enter the radius at the base of the cone: "))
        base_area = math.pi * radius ** 2
        print(f"{figure} {para} is {base_area}")
    if para == "Length of cone shaping":
        radius = float(input("Enter the radius at the base of the cone: "))
        height = float(input("Enter height: "))
        side_area_side = math.sqrt(radius ** 2 + height ** 2)
        print(f"{figure} {para} is {side_area_side}")
    if para == "Between cone shaping and base angle":
        radius = float(input("Enter the radius at the base of the cone: "))
        side_area_side_n_base_angle = height / radius
        print(f"{figure} {para} is {side_area_side_n_base_angle}")
    else:
        print("Sike nibba you thought")

elif figure == "Octahedron":
    if para == "Volume":
        side = float(input("Enter the side of the octahedron: "))
        volume = (math.sqrt(2) * side ** 3) / 3
        print(f"{figure} {para} is {volume}")
    if para == "Area":
        side = float(input("Enter the side of the octahedron: "))
        area = 2 * math.sqrt(3) * side ** 2
        print(f"{figure} {para} is {area}")
    if para == "Radius of circumcircle":
        side = float(input("Enter the side of the octahedron: "))
        rad_int = (math.sqrt(2) * side) / 2
        print(f"{figure} {para} is {rad_int}")
    if para == "Radius of the incircle":
        side = float(input("Enter the side of the octahedron: "))
        rad_out = (math.sqrt(6) * side) / 6
        print(f"{figure} {para} is {rad_out}")
    else:
        print("Not sheesh")