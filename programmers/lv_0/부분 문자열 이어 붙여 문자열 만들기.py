def solution(my_strings, parts):
    res = ''
    for my_string, part in zip(my_strings, parts):
        res += my_string[part[0] : part[1] + 1]
    return res
