def solution(message):
    # 1. 글자 한 자당 가로 2cm => 글자수*2 편지 최소 가로 길이 2. 가로로만 작성 3. message  
    # 글자 수*2 구해서 return
    #return len(message)*2
    count = 0
    for alphabet in message:
        count = count + 1
    return count*2