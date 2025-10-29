def solution(numbers):
    #numbers 중 두 개 곱해 만드는 최댓값 return
    #가장 큰 수 골라서 , 곱하고 , return
    numbers.sort()
    #오름차순으로 정렬한 뒤,
    return numbers[-1]*numbers[-2]
#오름차순일 땐 뒤에 잇는 게 가장 크니까 가장 큰 거 , 그 다음 것 -1, -2로 => 두 개 곱하기