STR, DEX, INT, LUK, n = map(int, input().split())
total_status = STR + DEX + INT + LUK

if total_status < (4 * n): print((4 * n) - total_status)
else: print(0)
