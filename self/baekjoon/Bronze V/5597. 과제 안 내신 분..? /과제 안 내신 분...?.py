# 학생들의 번호를 리스트에 저장 후
std = [i for i in range(1,31)] 
for _ in range(28):
  # 학생들의 번호를 입력받고
  a = int(input())    
  # 입력받은 숫자를 리스트에서 지운 뒤
  std.remove(a)
# 작은 번호부터 출력
print(min(std))
print(max(std))
