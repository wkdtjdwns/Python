for _ in range(int(input())):
    abc = [*map(int, input().split(' '))]
    print(int(9.23076 * ((26.7 - abc[0]) ** 1.835))
          + int(1.84523 * ((abc[1] - 75) ** 1.348))
          + int(56.0211 * ((abc[2] - 1.5) ** 1.05))
          + int(4.99087 * ((42.5 - abc[3]) ** 1.81))
          + int(0.188807 * ((abc[4] - 210) ** 1.41))
          + int(15.9803 * ((abc[5] - 3.8) ** 1.04))
          + int(0.11193 * ((254 - abc[6]) ** 1.88)))
