n, k = map(int, input().split())
num_str = input()
new_num_str = ""

for i in range(n - k + 1):
    cur_num = int(num_str[i])
    next_num = int(num_str[i + 1])
    print(f"cur_num: {cur_num}, next_num: {next_num}")
    if cur_num >= next_num:
        new_num_str += str(cur_num)
        print(new_num_str)

print(new_num_str)
