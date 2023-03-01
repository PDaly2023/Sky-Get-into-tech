#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

partA = ""

for I in Belgium:
    partA = partA + "*"
print(partA)

print(len(Belgium))
print(len(partA))

partB = Belgium.replace(",",":")
print(partB)

partC = Belgium.split(",")
print(int(partC[1]) + int(partC[3]))
print(partC)

#OR
count = 0
#as we know where to stop (4th item), we can stop the loop after 4 loops
for i in partC[:4]:
    if i.isdecimal():
        count = count + int(i)
print(count)
