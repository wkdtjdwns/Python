for i in range(int(input())):
    abc = sorted(map(int, input().split(' ')))
    if abc[0] ** 2 + abc[1] ** 2 == abc[2] ** 2:
        print(f"Scenario #{i+1}:")
        print("yes\n")

    else:
        print(f"Scenario #{i+1}:")
        print("no\n")
