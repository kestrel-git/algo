def solution(A, B):
    return (B*2).find(A)
    
#     st_len = len(A)
#     for i in range(st_len):
#         tmp_a = A[-i:] + A[:st_len-i] if i != 0 else A
#         if tmp_a == B:
#             return i
#     return -1
