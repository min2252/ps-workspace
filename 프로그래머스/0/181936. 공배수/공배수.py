def solution(number, n, m):
    if (number % n == 0) and (number % m == 0 ):
        #두 조건이 모두 참이면 1, 아니면 0을 반환
        answer = 1
    else: 
        answer = 0
    return answer