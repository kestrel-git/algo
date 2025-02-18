def solution(s):
    result = 0
    sl = s.split()
    
    for i in range(len(sl)):
        result += int(sl[i]) if sl[i] != 'Z' else -int(sl[i-1])
    
    return result
