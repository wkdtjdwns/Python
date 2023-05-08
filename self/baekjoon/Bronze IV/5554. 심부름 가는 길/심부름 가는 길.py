home_school = int(input())
school_pc = int(input())
pc_academy = int(input())
academy_home = int(input())
x = (home_school + school_pc + pc_academy + academy_home) // 60
y = (home_school + school_pc + pc_academy + academy_home) % 60
print(x)
print(y)
