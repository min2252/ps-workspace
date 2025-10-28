def solution(n, k):
    # 양꼬치 n인분..? 음료수를 k개 먹었으면.. 
    original = (n * 12000) + (k * 2000)
    # 10인분 먹으면??...
    # 30 -> 3 78 -> 7
    discount = (n // 10) * 2000
    answer = original - discount
    return answer