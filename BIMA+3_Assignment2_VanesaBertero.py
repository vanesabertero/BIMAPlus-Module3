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
    print("Enter x and y coordinates of polygon points, ordered counter clockwise...")

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
    
    n = numOfPoints
    Ax = 0.0
    for i in range(0, numOfPoints):
         Ax = Ax + ((pointsX[(i+1)%n] + pointsX[i]) * (pointsY[(i+1)%n] - pointsY[i])) 
    Ax = Ax * 0.5 
       # Example solution to understand use of % in python (coordinates 1,1; 3,1; 3,3; 1;3) --> polygon square, 2x2
       # Ax = Ax + ((x[(0+1)%4] + x[0]) * (y[(0+1)%4] - y[0])) = ((x[1] + x[0]) * (y[1] - y[0])) = (3+1)(1-1)=0
       # Ax = Ax + ((x[(1+1)%4] + x[1]) * (y[(1+1)%4] - y[1])) = ((x[2] + x[1]) * (y[2] - y[1])) = (3+3)(3-1)=12
       # Ax = Ax + ((x[(2+1)%4] + x[2]) * (y[(2+1)%4] - y[2])) = ((x[3] + x[2]) * (y[3] - y[2])) = (1+3)(3-3)=0
       # Ax = Ax + ((x[(3+1)%4] + x[3]) * (y[(3+1)%4] - y[3])) = ((x[0] + x[3]) * (y[0] - y[3])) = (1+1)(1-3)=-4
       # Ax = Ax + (0 + 12 + 0 -4)
       # Ax = 0.0 + 8
    # Ax = Ax * 0.5 
    # Ax = 4  ---> Correct
    print(f"{'Ax:'} {Ax:>10.2f}")

    Sx = 0.0
    for i in range(0, numOfPoints):
        Sx = Sx + ((pointsX[(i+1)%n] - pointsX[i]) * (pointsY[(i+1)%n]**2 + pointsY[i] * pointsY[(i+1)%n] + pointsY[i]**2))
    Sx = Sx * (-1/6)
    print(f"{'Sx:'} {Sx:>10.2f}")
    
    Sy = 0.0
    for i in range(0, numOfPoints):
        Sy = Sy + ((pointsY[(i+1)%n] - pointsY[i]) * (pointsX[(i+1)%n]**2 + pointsX[i] * pointsX[(i+1)%n] + pointsX[i]**2))
    Sy = Sy * (1/6)
    print(f"{'Sy:'} {Sy:>10.2f}")
    
    Ix = 0.0
    for i in range(0, numOfPoints):
        Ix = Ix + ((pointsX[(i+1)%n] - pointsX[i]) * (pointsY[(i+1)%n]**3 + pointsY[(i+1)%n]**2 * pointsY[i] + pointsY[(i+1)%n] * pointsY[i]**2 + pointsY[(i+1)%n]**3))
    Ix = Ix * (-1/12)
    print(f"{'Ix:'} {Ix:>10.2f}")
    
    Iy = 0.0
    for i in range(0, numOfPoints):
        Iy = Iy + ((pointsY[(i+1)%n] - pointsY[i]) * (pointsX[(i+1)%n]**3 + pointsX[(i+1)%n]**2 * pointsX[i] + pointsX[(i+1)%n] * pointsX[i]**2 + pointsX[(i+1)%n]**3))
    Iy = Iy * (1/12)
    print(f"{'Iy:'} {Iy:>10.2f}")
    
    Ixy = 0.0
    for i in range(0, numOfPoints):
        Ixy = Ixy + (pointsY[(i+1)%n] - pointsY[i]) * (pointsY[(i+1)%n] * (3*pointsX[(i+1)%n]**2 + 2*pointsX[(i+1)%n] * pointsX[i] + pointsX[i]**2) + pointsY[i] * (3*pointsX[i]**2 + 2*pointsX[(i+1)%n] * pointsX[i] + pointsX[(i+1)%n]**2))
    Ixy = Ixy * (-1/24)
    print(f"{'Ixy:'} {Ixy:>9.2f}")
    
    xT = Sy / Ax
    print(f"{'xT:'} {xT:>10.2f}")
    
    yT = Sx / Ax
    print(f"{'yT:'} {yT:>10.2f}")
    
    IxT = Ix - (yT**2 * Ax )
    print(f"{'IxT:'} {IxT:>9.2f}")
    
    IyT = Iy - (xT**2 * Ax )
    print(f"{'IyT:'} {IyT:>9.2f}")
    
    IxyT = Ixy + ( xT * yT * Ax )
    print(f"{'IxyT:'} {IxyT:>8.2f}")

    print()
    print("This is the end!")
