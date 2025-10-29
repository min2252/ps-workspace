def solution(array, height):
    # 머쓱이네 반 친구들 키 array, 머쓱이의 키 height // 머쓱이보다 키 큰 사람 수 return
    count = 0
    # 머쓱이보다 키 큰 사람을 카운트 해야 됨
    for i in array:
        if i > height:
        # 머쓱이보다 키가 크다면
            count += 1
            # 하나를더해야됨
    return count