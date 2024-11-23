num = int(input())

for i in range(num):
    for b in range(num - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
