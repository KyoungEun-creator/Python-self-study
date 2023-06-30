'''
당신은 택시 기사
50명의 승객과 매칭 기회가 있을 때, 총 승객 수를 구하는 프로그램을 작성하라

조건1: 승객별 운행 소요 시간은 5~50분 사이의 난수
조건2: 당신은 5~15분 사이의 승객만 매칭

(출력문 예제)
[ㅇ] 1번째 손님 (소요시간: 15분)
[ ] 2번째 손님 (소요시간: 50분)
[ㅇ] 3번째 손님 (소요시간: 5분)
...
[ ] 50번째 손님 (소요시간: 16분)

총 탑승 승객: 2명
'''

# 내 답안

from random import *
cnt = 0                     # 총 승객 수
real_cust = 0               # 실제 탑승객 수
for i in range(1,51):       # 승객: 1~50명
    time = randrange(5,51)  # 소요시간: 5~50분
    cnt += 1
    if 5 <= time <=15:
        print("[{0}] {1}번째 손님 (소요시간: {2}분)".format("o",cnt,time))
        real_cust += 1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(cnt,time))
print("총 탑승 승객: {0}".format(real_cust))


# 예시 답안

from random import *
cnt = 0                     # 총 탑승객 수
for i in range(1,51):       # 승객: 1~50명
    time = randrange(5,51)  # 소요시간: 5~50분
    if 5 <= time <=15:
        print("[ㅇ] {0}번째 손님 (소요시간: {1}분)".format(i,time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(i,time))
print("총 탑승 승객: {0}".format(cnt))

