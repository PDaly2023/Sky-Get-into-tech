from math import pi, tan, cos

g = 9.81 #Acceleration due to gravity in m/s units)
v0 =  44 #initial velocity in m/s unit
theta = 80 * (pi/180) #elevation angle in radians
x = 0.5 #the horizontal distance travelled
y0 = 1 #height of the barrel in m units

print("""
when a barrel at height 1m, after a horizontal distance of 0.5m, 
an elevation of 80 degrees, and an initial velocity of 44 m/s, 
what is the height of the projectile?""")
print()

print("Using theta = deg * (pi/180) to convert fromdegrees to radians")
print("")
print("theta = ", theta)
print("tan theta = ", tan(theta))
print("tan theta * x (0.5) = ", x * tan(theta))
print("y0(1) + x(0.5 * tan theta = ", y0 + (x * tan(theta)))
print("")
print("g(9.81) * x(0.5)^2 = ", g * (x ** 2))
print("2 * ((v0(1) * cos(theta)) ** 2 = ", 2 * ((v0 * cos(theta)) ** 2))

y= (y0 + x * tan(theta)) - ((g * (x ** 2)) / (2 * ((v0 * cos(theta)) ** 2))) #doesn't really need the brackets - added to make clearer

print("")
print ("the height of the projectile is:", y, "m")