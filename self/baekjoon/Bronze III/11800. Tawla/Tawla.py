name = {
    1: "Yakk",
    2: "Doh",
    3: "Seh",
    4: "Ghar",
    5: "Bang",
    6: "Sheesh"
}

same = {
    1: "Habb Yakk",
    2: "Dobara",
    3: "Dousa",
    4: "Dorgy",
    5: "Dabash",
    6: "Dosh"
}

results = []
for i in range(1, int(input()) + 1):
    a, b = map(int, input().split(' '))

    if a == b:
        result = f"Case {i}: {same[a]}"
        
    elif (a == 6 and b == 5) or (a == 5 and b == 6):
        result = f"Case {i}: Sheesh Beesh"
        
    else:
        result = f"Case {i}: {name[max(a, b)]} {name[min(a, b)]}"

    results.append(result)

for result in results:
    print(result)
