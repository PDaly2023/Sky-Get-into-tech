planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597879,
           'Mars': 227.94
}

#{d} = treats the arguement as an integer
#{s} = treats the arguement as a string
#{f} = treats the arguement as a float

#1 = start at 1 (treat beginning of dictionary as 1 not 0)
for i, key in enumerate (planets.keys(), 1):
    #0 1 and 2 not needed but added for clarity - selects correct items
    print("{0:2d} {1:<10s} {2:06.2f} Gm".format (i, key, planets[key]))

