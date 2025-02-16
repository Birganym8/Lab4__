import math


def degree_to_radian(degree):
    radian = math.radians(degree)
    return radian

degree = float(input("Input degree: "))


radian = degree_to_radian(degree)
print(f"Output radian: {radian:.6f}")
