
def trapezoid_area(height, base1, base2):
    area = (height * (base1 + base2)) / 2
    return area


height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))


area = trapezoid_area(height, base1, base2)

print(f"Expected Output: {area}")
