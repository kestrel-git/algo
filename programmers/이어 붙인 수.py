def solution(num_list):
    odd_num = even_num = 0
    
    for num in num_list:
        if num % 2:
            odd_num = odd_num * 10 + num
        else:
            even_num = even_num * 10 + num
    
    return odd_num + even_num
