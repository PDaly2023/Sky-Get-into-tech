from math import pi, tan, cos


def projectile_height(y0, v0, x, theta):
    y = y0 + x * tan(theta) - (9.81 * (x ** 2)) / (2 * ((v0 * cos(theta)) ** 2))
    return round(y, 2)


y0 = 1
v0 = 44
x = 0.5
theta = 80 * (pi / 180)

print("The height of the projectile is:", projectile_height(y0, v0, x, theta), "m")
