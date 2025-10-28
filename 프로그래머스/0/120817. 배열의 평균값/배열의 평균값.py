def solution(numbers):
    # total:sum(numbers)/numbers
    #numbers를 다 더하고 나눠야 평균값이나오는ep
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count