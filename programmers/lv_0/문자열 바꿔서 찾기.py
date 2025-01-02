def solution(myString, pat):
    converted_pat = ''.join(['A' if s == 'B' else 'B' for s in pat])
    return int(converted_pat in myString)
