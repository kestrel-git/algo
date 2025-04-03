from collections import defaultdict

def solution(array):
    freq_dict = defaultdict(int)
    freq_max = 0
    
    for num in array:
        # 등장 개수 계산
        freq_dict[num] += 1
    
        # 가장 많이 등장한 개수 저장
        if freq_dict[num] > freq_max:
            freq_max = freq_dict[num]
    
    # 최빈값 찾기
    numbers = [key for key, freq in freq_dict.items() if freq == freq_max]
    
    return numbers[0] if len(numbers) == 1 else -1
