def solution(str1, str2):
    #str1  안에 str2가 있으면 1을, 없다면 2를 return
    # 파이썬의 'in' 문자열 포함 여부 true/false로 반환
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    return answer