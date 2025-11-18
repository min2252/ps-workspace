def solution(money):
    #아메리카노 한잔 가격
    price = 5500
    count = money // price
    #최대로 살 수 있는 잔 수 
    change = money % price
    #잔돈
    answer = [ count, change]
    #잔 수, 잔돈 형태로 반환
    return answer