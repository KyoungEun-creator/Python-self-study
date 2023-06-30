'''
customer = "최재림"
index = 5
while index >= 1:
    print("{0}님 커피 준비됐습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 폐기처분되었습니다")
'''

'''
customer = "손석구"
index = 1
while True:
    print("{0}님 커피 준비됐습니다. 픽업대로 오세요. (호출 {1}회)".format(customer, index))
    index += 1 # 무한루프 (종료 원할 시 ctl+C)
'''

customer = "윤성빈"
person = "unknown"

while person != customer:
    print("{0}님 커피 준비됐습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")