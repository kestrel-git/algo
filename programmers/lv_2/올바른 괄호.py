def solution(s):
    p = []
    
    for c in s:
        if c == '(':                 # 열린 괄호일 때, 리스트에 추가
            p.append(c)
        elif p[-1:] == ['(']:        # 닫힌 괄호일 때, 직전에 열린 괄호가 있으면 리스트에서 제거
            p.pop()
        else:                        # 닫힌 괄호일 때, 직전에 열린 괄호가 없는 경우 False 리턴
            return False
    
    return True if not p else False  # 리스트가 비어 있으면 True, 비어 있지 않으면 False 리턴
