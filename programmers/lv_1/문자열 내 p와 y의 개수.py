import re

def solution(s):
    p_list = re.findall(r'p|P', s)
    y_list = re.findall(r'y|Y', s)
    return len(p_list) == len(y_list)
