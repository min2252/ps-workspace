def solution(num_list):
    reverse_list = []
    length  = len(num_list)
    for index in range (length-1, -1, -1):
        #이걸리버스리스트에넣자
        reverse_list.append(num_list[index])
    return reverse_list
    #뒤에서 앞으로 하게 하고 싶음ㄴ데 그럴려면 -1을 하면 되지않나