def solution(n, lost, reserve):
    #각각의 여집합 찾아주기
    setReserve = set(reserve) - set(lost)
    setLost = set(lost) - set(reserve)
    #좌측에 있는 사람부터 주기
    for i in setReserve :
        if i-1 in setLost :
            setLost.remove(i-1)
        elif i+1 in setLost :
            setLost.remove(i+1)
    answer = n-len(setLost)
    return answer