
#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
b_list = Belgium.split(",")

print("'" * len(Belgium))
print(":".join(b_list))
print(int(b_list[1]) + int(b_list[3]))