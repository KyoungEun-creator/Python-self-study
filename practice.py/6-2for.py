for waiting_num in [1,2,3,4,5]:
    print("대기번호: {0}".format(waiting_num))

for waiting_num in range(5):        # 0,1,2,3,4 순차적으로
    print("대기번호: {0}".format(waiting_num))

for waiting_num in range(1,6):        # 1,2,3,4,5 순차적으로
    print("대기번호: {0}".format(waiting_num))


starbucks = ["최재림", "손석구", "윤성빈"]
for customer in starbucks:
    print("{0}님 커피 준비되었습니다.".format(customer))
 