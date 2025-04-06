import re

def solution(polynomial):
    x_coef = sum(int(num or '1') for num in re.findall(r'(\d*)x', polynomial))
    constant = sum(int(num) for num in re.findall(r'\b\d+\b', polynomial))

    x_str = f'{x_coef}x' if x_coef > 1 else 'x'
    x_str = x_str if x_coef else ''
    
    return x_str + \
           (' + ' if x_coef and constant else '') + \
           (f'{constant}' if constant else '')
