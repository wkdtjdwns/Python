a, b = None, None
for i in range(1, 10):
    if a is None:
        print(f"? A {i}", flush=True)
        response = int(input().strip())
        if response == 1:
            a = i

    if b is None:
        print(f"? B {i}", flush=True)
        response = int(input().strip())
        if response == 1:
            b = i

    if a is not None and b is not None:
        break

print(f"! {a + b}", flush=True)
