# 입력
n = int(input())
nums = list(map(int, input().split()))

# 최솟값, 최댓값 초기화
min = max = nums[0]

for val in nums:
    if val < min:
        min = val
    if max < val:
        max = val

# 출력
print(min, max)
