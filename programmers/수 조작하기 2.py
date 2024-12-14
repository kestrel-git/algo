def solution(numLog):
    num_con = {1: "w", -1: "s", 10: "d", -10: "a"}
    res = ""
    for idx in range(1, len(numLog)):
        diff = numLog[idx] - numLog[idx - 1]
        res += num_con[diff]
    return res
