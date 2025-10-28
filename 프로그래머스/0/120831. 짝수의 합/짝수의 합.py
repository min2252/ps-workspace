def solution(n):
#     # 음.. n 이하의 짝수를 모두 더한 값...???
#     # 짝수를 어떻게 정의해야되징 i = 1 -> 0 2 
#     # 짝수만 뽑을수없나
    total = 0
    for i in range(0, n + 1):
        if i % 2 == 0:
        # i가 짝수라면, 을 어케 적어야되지?
            total += i
    return total
    # 1부터 n까지 숫자 중에 짝수를 total에 더하기 를 해야 되는대.. 1부터 100까지 출력하도록 