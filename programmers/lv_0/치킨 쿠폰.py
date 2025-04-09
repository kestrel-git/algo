def solution(chicken):
    return max(chicken - 1, 0) // 9
    
#     EXCHANGE_RATE = 10
#     answer = 0
    
#     while chicken >= EXCHANGE_RATE:
#         answer += chicken // EXCHANGE_RATE
#         chicken = int(chicken / EXCHANGE_RATE) + chicken % EXCHANGE_RATE
    
#     return answer
