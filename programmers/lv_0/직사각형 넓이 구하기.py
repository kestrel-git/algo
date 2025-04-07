def solution(dots):
    xs = list(set(dot[0] for dot in dots))
    ys = list(set(dot[1] for dot in dots))
    return abs(xs[0] - xs[1]) * abs(ys[0] - ys[1])
