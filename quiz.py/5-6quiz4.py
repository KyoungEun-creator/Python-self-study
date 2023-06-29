'''
댓글 작성자들 중 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받게 된다. 
추첨 프로그램을 작성하라.

조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3: random 모듈의 shuffle과 sample을 활용


(출력 예제)
-- 당첨자 발표 --
치킨 당첨자: 1 
커피 당첨자: [2, 3, 4]
-- 축하합니다 --
'''

# # random 모듈 활용 예시
# from random import *
# list = [1,2,3,4,5]
# print(list)
# shuffle(list)
# print(list)
# print(sample(list,1))       # list 안에서 1개 추첨 [3]



# 내 답안

from random import *
users = range(1,21)
print(type(users))
users = list(users)
print(users)

shuffle(users)
print(users)

chicken = sample(users,1)
chicken = set(chicken)
print(chicken)
users = set(users)
coffee = sample(users - chicken, 3)
print(coffee)

print("-- 당첨자 발표 -- \n 치킨 당첨자: ", chicken, "\n 커피 당첨자: ", coffee, "\n -- 축하합니다 --")


# 예시 답안 

from random import *
users = range(1,21)
users = list(users)
shuffle(users)
print(users)

winners = sample(users, 4)
print(winners)               # 뽑힌 네 명 중에서 한 명은 치킨, 세 명은 커피 주기로 함

print("-- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(winners[0])) 
print("커피 당첨자: {0}".format(winners[1:]))
print("-- 축하합니다 --")