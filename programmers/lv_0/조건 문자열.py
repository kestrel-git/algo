def solution(ineq, eq, n, m):
    eq = "" if eq == "!" else eq
    return int(eval(f"{n} {ineq}{eq} {m}"))
