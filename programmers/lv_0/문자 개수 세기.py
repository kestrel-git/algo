import string

def solution(my_string):
    res = dict.fromkeys(string.ascii_uppercase + string.ascii_lowercase, 0)

    for s in my_string:
        res[s] += 1
    
    return list(res.values())
