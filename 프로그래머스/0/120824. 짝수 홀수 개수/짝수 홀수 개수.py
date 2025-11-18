def solution(num_list):
    a = 0
    b = 0
    for num in num_list:
        if num % 2 == 0:
            a = a + 1
            # 짝수 카운트 1 증가 
        else:
            b = b + 1
    return [a, b]