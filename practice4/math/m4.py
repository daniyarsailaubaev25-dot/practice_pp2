from math import sin, radians

a = float(input())
b = float(input())
angle_deg = float(input())

area = a * b * sin(radians(angle_deg))
print(area)