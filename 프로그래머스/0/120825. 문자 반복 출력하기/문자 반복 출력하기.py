def solution(my_string, n):
    answer = ''
    for i in my_string: 
        # 현재 문자 char를 n번 반복해서 answer에 이어붙임
        answer += (i * n)
    return answer

#       근데 헷갈렬요