def solution(code):
    mode = 0
    ret = ''
    
    for idx in range(len(code)):
        if code[idx] != '1':
            if idx % 2 == mode:
                ret += code[idx]
        else:
            mode ^= 1
    
    return ret or 'EMPTY'
