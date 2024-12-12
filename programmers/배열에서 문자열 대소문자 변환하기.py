def solution(strArr):
    for i, st in enumerate(strArr):
        if i % 2 != 0:
            strArr[i] = st.upper()
        else:
            strArr[i] = st.lower()
    return strArr
