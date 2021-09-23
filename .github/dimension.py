print("Enter dimensions for room in feet")
L = float(input("Length of room"))
W = float(input("Width of room"))
H = float(input("Height of room "))

# Find the area of the wall, ceiling, and total area that needs paint.

areaWall1 = 2*W*H
areaWall2= 2*L*H
areaCeiling = L*W
totalArea = areaCeiling + areaWall2 +areaWall1

print("Total area  required in sq is: %.2f"% totalArea)

# calculation of amount of paint needed
totalPaint = totalArea/350
totalPrimer = totalArea / 200

print("Total amount of paint needed: %.2f gallons" % totalPaint)
print("Total amount of primer needed: %.2f gallons" % totalPrimer)



