def solution(rank, attendance):
    students = sorted([(rnk, idx) for idx, rnk in enumerate(rank) if attendance[idx]])
    return 10000 * students[0][1] + 100 * students[1][1] + students[2][1]
