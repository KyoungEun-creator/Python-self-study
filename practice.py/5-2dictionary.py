# {key: value}

from time import process_time_ns


cabinet = {1:'a', 2:'b'}
print(cabinet[1])           # a
print(cabinet[2])           # b
print(cabinet.get(1))       # a

'''
print(cabinet[5])           # error와 함께 프로그램 종료시킴
print('hi')
'''
print(cabinet.get(5))       # None 출력 (프로그램 종료X)
print('hi')
print(cabinet.get(5, 'unavailable'))       # 5가 없을 경우 None 대신 출력 

# key in 변수
print(3 in cabinet)         # False
print(1 in cabinet)         # True

# 새로운 값 추가
cabinet[3] = 'c'
print(cabinet)              # {1: 'a', 2: 'b', 3: 'c'}

# 기존 값 변경
cabinet[1] = 'd'
print(cabinet)              # {1: 'd', 2: 'b', 3: 'c'} 

# 값 삭제
del cabinet[1]
print(cabinet)              # {2: 'b', 3: 'c'}

# key만 출력
print(cabinet.keys())       # dict_keys([2, 3])

# value만 출력
print(cabinet.values())     # dict_values(['b', 'c'])

# key, value 쌍으로 출력
print(cabinet.items())      # dict_items([(2, 'b'), (3, 'c')])

# 모든 값 삭제
cabinet.clear()
print(cabinet)              # {}