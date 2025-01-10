def solution(strArr):
    len_list = [0] * 30
    
    for s in strArr:
        len_list[len(s)-1] += 1
        
    return max(len_list)
