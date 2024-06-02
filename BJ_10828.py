import sys

input_size = int(sys.stdin.readline())
stack = []

for _ in range(input_size):
    cur_input = sys.stdin.readline().split()

    if cur_input[0] == "push":
        stack.append(cur_input[1])

    elif cur_input[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif cur_input[0] == "size":
        print(len(stack))

    elif cur_input[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif cur_input[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
