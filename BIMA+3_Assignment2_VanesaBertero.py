# The Python program calculates different geometrical characteristics of a polygon shape

import math

print("The Python program calculates different geometrical characteristics of a polygon shape")
print()

numOfPoints = int(input("Enter the number of polygon points: "))

if numOfPoints < 3:
    letsGo = 0
    print("Not possible to calculate polygon. Minimun number of points is 3.")
    print("End.")
else:
    letsGo = 1
    print("Enter x and y coordinates of polygon points...")

if letsGo == 1:
    # A list that stores all entered point coordinates. Its empty at start.
    pointsX = []
    pointsY = []

    # Input coordinates points
    for i in range(numOfPoints):
        r = float(input(f"Point(x)[{i+1}]: "))
        pointsX.append(r)
        r = float(input(f"Point(y)[{i+1}]: "))
        pointsY.append(r)

    # Print a table of entered data and calculated values
    print()
    print(f"{'Point':>5} {'x':>10} {'y':>10}")
    print("-" * 27)
    for i in range(numOfPoints):
        print(f"{i + 1:5} {pointsX[i]:10.2f} {pointsY[i]:10.2f}")

    # Calculate geometric characteristics (all the formulas)
    print()
    print("Geometric characteristics:")
    
    Ax = 0.0
    for i in range(0, numOfPoints-1):
        Ax = Ax + ((pointsX[i+1] + pointsX[i]) * (pointsY[i+1] - pointsY[i])) 
    Ax = Ax * 0.5
    if Ax < 0:
        Ax = -1*Ax
    print(f"{'Ax:'} {Ax:10.2f}")

    Sx = 0.0
    for i in range(0, numOfPoints-1):
        Sx = Sx + ((pointsX[i+1] - pointsX[i]) * (pointsY[i+1]**2 + pointsY[i] * pointsY[i+1] + pointsY[i]**2))
    Sx = Sx * (-1/6)
    print(f"{'Sx:'} {Sx:10.2f}")
    
    Sy = 0.0
    for i in range(0, numOfPoints-1):
        Sy = Sy + ((pointsY[i+1] - pointsY[i]) * (pointsX[i+1]**2 + pointsX[i] * pointsX[i+1] + pointsX[i]**2))
    Sy = Sy * (1/6)
    print(f"{'Sy:'} {Sy:10.2f}")
    
    Ix = 0.0
    for i in range(0, numOfPoints-1):
        Ix = Ix + ((pointsX[i+1] - pointsX[i]) * (pointsY[i+1]**3 + pointsY[i+1]**2 * pointsY[i] + pointsY[i+1] * pointsY[i]**2 + pointsY[i+1]**3))
    Ix = Ix * (-1/12)
    print(f"{'Ix:'} {Ix:10.2f}")
    
    Iy = 0.0
    for i in range(0, numOfPoints-1):
        Iy = Iy + ((pointsY[i+1] - pointsY[i]) * (pointsX[i+1]**3 + pointsX[i+1]**2 * pointsX[i] + pointsX[i+1] * pointsX[i]**2 + pointsX[i+1]**3))
    Iy = Iy * (1/12)
    print(f"{'Iy:'} {Iy:10.2f}")
    
    Ixy = 0.0
    for i in range(0, numOfPoints-1):
        Ixy = Ixy + (pointsY[i+1] - pointsY[i]) * (pointsY[i+1] * (3*pointsX[i+1]**2 + 2*pointsX[i+1] * pointsX[i] + pointsX[i]**2) + pointsY[i] * (3*pointsX[i]**2 + 2*pointsX[i+1] * pointsX[i] + pointsX[i+1]**2))
    Ixy = Ixy * (-1/24)
    print(f"{'Ixy:'} {Ixy:10.2f}")
    
    xT = 0.0
    for i in range(0, numOfPoints-1):
        xT = Sy / Ax
    print(f"{'xT:'} {xT:10.2f}")
    
    yT = 0.0
    for i in range(0, numOfPoints-1):
        yT = Sx / Ax
    print(f"{'yT:'} {yT:10.2f}")
    
    IxT = 0.0
    for i in range(0, numOfPoints-1):
        IxT = Ix - (yT**2 * Ax )
    print(f"{'IxT:'} {IxT:10.2f}")
    
    IyT = 0.0
    for i in range(0, numOfPoints-1):
        IyT = Iy - (xT**2 * Ax )
    print(f"{'IyT:'} {IyT:10.2f}")
    
    IxyT = 0.0
    for i in range(0, numOfPoints-1):
        IxyT = Ixy + ( xT * yT * Ax )
    print(f"{'IxyT:'} {IxyT:10.2f}")

    print()
    print("End.")




