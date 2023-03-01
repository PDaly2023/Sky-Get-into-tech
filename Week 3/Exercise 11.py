#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

partA = ""

for I in Belgium:
    partA = partA + "'"
print(partA)


#checking
#print(len(Belgium) == len(partA))

partB = Belgium.replace(",",":")
print(partB)


partC = Belgium.split(",")
print(int(partC[1]) + int(partC[3]))

