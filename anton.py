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
    elif para == "Surface area всего параллелипипеда":
        side_1 = float(input("Enter the length at the base of the parallelepiped: "))
        side_2 = float(input("Enter the width at the base of the parallelepiped: "))
        height = float(input("Enter the height at the base of the parallelepiped: "))
        area = 2 * (side_1 * side_2 + height * side_2 + side_1 * height)
        print(f"{figure} {para} is {area}")
    elif para == "Площадь основания параллелипипеда":
        side_1 = float(input("Enter the length at the base of the parallelepiped: "))
        side_2 = float(input("Enter the width at the base of the parallelepiped: "))
        base_area = math.sqrt(side_1 ** 2 + side_2 ** 2)
        print(f"{figure} {para} is {base_area}")
    elif para == "Площадь меньшей по ширине стороны параллелипипеда":
        side_2 = float(input("Enter the width at the base of the parallelepiped: "))
        height = float(input("Enter the height at the base of the parallelepiped: "))
        side_area_1 = math.sqrt(side_2 ** 2 + height ** 2)
        print(f"{figure} {para} is {side_area_1}")
    elif para == "Площадь большей по ширине стороны параллелипипеда":
        side_1 = float(input("Enter the length at the base of the parallelepiped: "))
        height = float(input("Enter the height at the base of the parallelepiped: "))
        side_area_2 = math.sqrt(side_1 ** 2 + height ** 2)
        print(f"{figure} {para} is {side_area_2}")
    elif para == "Диагональ основания":
        side_1 = float(input("Enter the length at the base of the parallelepiped: "))
        side_2 = float(input("Enter the width at the base of the parallelepiped: "))
        base_diagonal = math.sqrt(side_1 ** 2 + side_2 ** 2)
        print(f"{figure} {para} is {base_diagonal}")
    elif para == "Диагональ меньшей по ширине стороны параллелипипеда":
        side_2 = float(input("Enter the width at the base of the parallelepiped: "))
        height = float(input("Enter the height at the base of the parallelepiped: "))
        side_diagonal_1 = math.sqrt((side_2 ** 2 + height ** 2))
        print(f"{figure} {para} is {side_diagonal_1}")
    elif para == "Диагональ меньшей по ширине стороны параллелипипеда":
        side_1 = float(input("Enter the length at the base of the parallelepiped: "))
        height = float(input("Enter the height at the base of the parallelepiped: "))
        side_diagonal_2 = math.sqrt((side_1 ** 2 + height ** 2))
        print(f"{figure} {para} is {side_diagonal_2}")
    elif para == "Диагональ всего параллелипипеда":
        side_1 = float(input("Enter the length at the base of the parallelepiped: "))
        side_2 = float(input("Enter the width at the base of the parallelepiped: "))
        height = float(input("Enter the height at the base of the parallelepiped: "))
        side_diagonal_2 = math.sqrt(math.sqrt(side_1 ** 2 + side_2 ** 2) + height ** 2)
        print(f"{figure} {para} is {side_diagonal_2}")
    else:
        print("You had mistaken")

elif figure == "Цилиндр":
    if para == "Volume":
        radius = float(input("Введите радиус окружности при основании: "))
        height = float(input("Введите высоту цилиндра: "))
        volume = math.pi * radius ** 2 * height
        print(f"{figure} {para} is {volume}")
    elif para == "Площадь боковой поверхности":
        radius = float(input("Введите радиус окружности при основании: "))
        height = float(input("Введите высоту цилиндра: "))
        side_area = 2 * math.pi * radius * height
        print(f"{figure} {para} is {side_area}")
    elif para == "Площадь всей поверхности":
        radius = float(input("Введите радиус окружности при основании: "))
        height = float(input("Введите высоту цилиндра: "))
        area = 2 * math.pi * radius ** 2 + 2 * math.pi * radius * height
        print(f"{figure} {para} is {area}")
    elif para == "Площадь основания":
        radius = float(input("Введите радиус окружности при основании: "))
        base_area = math.pi * radius ** 2
        print(f"{figure} {para} is {base_area}")
    else:
        print("Mistake is your lifestyle")
        
elif figure == "Пирамида":
    if para == "Volume":
        side = float(input("Введите длину при основани пирамиды: "))
        height = float(input("Enter the width at the base of the parallelepiped: "))
        volume = 1/3 * height * side ** 2
        print(f"{figure} {para} is {volume}")
    if para == "Площадь боковой поверхности":
        side = float(input("Введите длину при основани пирамиды: "))
        height = float(input("Enter the width at the base of the parallelepiped: "))
        side_area = 1/2 * side * math.sqrt((1/2 * side) ** 2 + height ** 2) * 4
        print(f"{figure} {para} is {side_area}")
    if para == "Площадь всей поверхности":
        side = float(input("Введите длину при основани пирамиды: "))
        height = float(input("Enter the width at the base of the parallelepiped: "))
        area = 1/2 * side * math.sqrt((1/2 * side) ** 2 + height ** 2) * 4 + side ** 2
        print(f"{figure} {para} is {area}")
    if para == "Площадь основания":
        side = float(input("Введите длину при основани пирамиды: "))
        base_area = side ** 2
        print(f"{figure} {para} is {base_area}")
    if para == "Длина ребра":
        side = float(input("Введите длину при основани пирамиды: "))
        height = float(input("Enter the width at the base of the parallelepiped: "))
        side_area_side = math.sqrt((1/2 * side * math.sqrt(2)) ** 2 + height ** 2)
        print(f"{figure} {para} is {side_area_side}")
    if para == "Апофема":
        side = float(input("Введите длину при основани пирамиды: "))
        height = float(input("Enter the width at the base of the parallelepiped: "))
        apothegm = math.sqrt((1/2 * side) ** 2 + height ** 2)
        print(f"{figure} {para} is {apothegm}")
    if para == "Угол между боковой поверхностью и основанием":
        side = float(input("Введите длину при основани пирамиды: "))
        height = float(input("Enter the width at the base of the parallelepiped: "))
        side_n_base_angle = height / (1/2 * side)
        print(f"{figure} {para} is {side_n_base_angle}")
    if para == "Угол между ребром и основанием":
        side = float(input("Введите длину при основани пирамиды: "))
        side_area_side_n_base_angle = height / (1/2 * side * math.sqrt(2))
        print(f"{figure} {para} is {side_area_side_n_base_angle}")
    else:
        print("Daun")

elif figure == "Конус":
    if para == "Volume":
        radius = float(input("Введите длину при основани пирамиды: "))
        height = float(input("Введите высоту: "))
        volume = 1/3 * height * math.pi * radius ** 2
        print(f"{figure} {para} is {volume}")
    if para == "Площадь боковой поверхности":
        radius = float(input("Введите длину при основани пирамиды: "))
        height = float(input("Введите высоту: "))
        side_area = radius * math.pi * math.sqrt(radius ** 2 + height ** 2)
        print(f"{figure} {para} is {side_area}")
    if para == "Площадь всей поверхности":
        radius = float(input("Введите длину при основани пирамиды: "))
        height = float(input("Введите высоту: "))
        area = radius * math.pi * math.sqrt(radius ** 2 + height ** 2) + math.pi * radius ** 2
        print(f"{figure} {para} is {area}")
    if para == "Площадь основания":
        radius = float(input("Введите длину при основани пирамиды: "))
        base_area = math.pi * radius ** 2
        print(f"{figure} {para} is {base_area}")
    if para == "Длина образующей конуса":
        radius = float(input("Введите длину при основани пирамиды: "))
        height = float(input("Введите высоту: "))
        side_area_side = math.sqrt(radius ** 2 + height ** 2)
        print(f"{figure} {para} is {side_area_side}")
    if para == "Угол между образующей и основанием":
        radius = float(input("Введите длину при основани пирамиды: "))
        side_area_side_n_base_angle = height / radius
        print(f"{figure} {para} is {side_area_side_n_base_angle}")
    else:
        print("ОШИБКА: Ошибок нет")

elif figure == "октаедр":
    if para == "Volume":
        side = float(input("Введите сторону октаэдра: "))
        volume = (math.sqrt(2) * side ** 3) / 3
        print(f"{figure} {para} is {volume}")
    if para == "Площадь":
        side = float(input("Введите сторону октаэдра: "))
        area = 2 * math.sqrt(3) * side ** 2
        print(f"{figure} {para} is {area}")
    if para == "Радиус описанной окружности":
        side = float(input("Введите сторону октаэдра: "))
        rad_int = (math.sqrt(2) * side) / 2
        print(f"{figure} {para} is {rad_int}")
    if para == "Радиус вписанной окружности":
        side = float(input("Введите сторону октаэдра: "))
        rad_out = (math.sqrt(6) * side) / 6
        print(f"{figure} {para} is {rad_out}")
    else:
        print("ОШИБКА: Ошибок нет")