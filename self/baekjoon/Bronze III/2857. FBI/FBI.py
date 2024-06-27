people = [] 
for i in range(1, 6): 
    s = input()
    if "FBI" in s:
        people.append(i)

if people: print(*people)
else: print("HE GOT AWAY!")
