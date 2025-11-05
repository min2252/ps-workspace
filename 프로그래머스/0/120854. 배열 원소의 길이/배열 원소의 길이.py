def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i)) 
        # 처음 answer.append(i)를 했을 때 오류가 난 이유
        # answer.append(i)를 하면 문자열 자체를 answer에 넣는 거라 원래 리스트랑 같음
    return answer