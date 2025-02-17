def solution(emergency):
    dict_em = {}
    
    for i, em in enumerate(sorted(emergency, reverse=True)):
        dict_em[em] = i + 1
    
    return [dict_em[em] for em in emergency]
