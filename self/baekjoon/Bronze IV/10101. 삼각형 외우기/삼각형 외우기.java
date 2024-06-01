angleA = int(input())
angleB = int(input())
angleC = int(input())

if angleA + angleB + angleC == 180:
    
    if angleA == angleB == angleC == 60:
        print("Equilateral")
        
    elif (angleA == angleB) or (angleB == angleC) or (angleA == angleC):
        print("Isosceles")
    else:
        print("Scalene")
    
else:
    print("Error")
