def solution(slice, n):
#두 조각에서 열 조각까지 원하는 조각 수로 잘라줌 
# n명의 사람이 최소 한 조각 이상 피자 먹을려면 최소 몇판?i
# import.math써주자
    import math
    return math.ceil(n/slice)