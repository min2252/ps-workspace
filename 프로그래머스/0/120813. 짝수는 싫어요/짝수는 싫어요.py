def solution(n):
    answer = []
    for i in range(1, n+1, 2):
        #1부터 n까지 2씩 증가 -> 홀수만 나옴
        answer.append(i)
    return answer