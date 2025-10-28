def solution(n, t):
    # t시간동안 세균이 두 배씩 증가  
    # answer = 0
    # return answer
    for i in range(t):
        n *= 2
    return n
