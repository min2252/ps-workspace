def solution(my_string):
    reverse_string = ""
    for current in my_string:
        reverse_string = current + reverse_string
        #i를 앞에 붙여야 리버스로 생김 ex. john 1회 j 2회 oj 3회 hoj 4회 nhoj
    return reverse_string

    