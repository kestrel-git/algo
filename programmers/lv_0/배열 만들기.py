def solution(intStrs, k, s, l):
    answer = []
    
    for st in intStrs:
        n = int(st[s:s+l])
        if n > k:
            answer.append(n)
    
    return answer
