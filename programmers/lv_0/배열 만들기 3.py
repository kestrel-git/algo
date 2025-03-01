def solution(arr, intervals):
    answer = []
    for inter in intervals:
        answer.extend(arr[inter[0] : inter[1]+1])
    return answer
