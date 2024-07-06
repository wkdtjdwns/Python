std = [i for i in range(1,31)] 
for _ in range(28):
  a = int(input())    
  std.remove(a)
  
print(min(std))
print(max(std))
