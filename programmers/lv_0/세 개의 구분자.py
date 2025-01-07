import re

def solution(myStr):
    # return list(filter(len, re.split(r'[abc]', myStr))) or ["EMPTY"]
    return re.findall(r'[^abc]+', myStr) or ["EMPTY"]
