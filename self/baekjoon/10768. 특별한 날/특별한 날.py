month = int(input())
day = int(input())

if month < 2:
    print("Before")    
    
elif month == 2:
    if day < 18:
        print("Before")
        
    elif day > 18: 
        print("After")
        
    else: 
        print("Special")
else: 
    print("After")
