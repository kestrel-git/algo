from collections import Counter
    
def solution(before, after):
    return int(Counter(before) == Counter(after))

    # return int(sorted(before) == sorted(after))
