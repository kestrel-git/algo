def solution(s):
    s_dict = {}
    for ch in s:
        s_dict[ch] = s_dict[ch] + 1 if s_dict.get(ch) else 1
    return ''.join(sorted(k for k, v in s_dict.items() if v == 1))
