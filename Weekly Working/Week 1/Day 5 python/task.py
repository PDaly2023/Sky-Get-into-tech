#Task One
radius = int(input("Enter your radius: "))
try:
    float(radius)
    radius = int(radius)
    circumference = radius * 6.284
    print("the Circumference is",int(circumference))
    area = radius ** 2 * 3.142
    print("the Area is",area)
except:
    print("Not a number")

